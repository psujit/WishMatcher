package com.textmining.wishmatcher04;

import android.app.Activity;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class MainActivity extends Activity implements View.OnClickListener {

    TextView tvIsConnected;
    EditText etName;
    Button btnPost;

    private static final String TAG_RESULT = "result";

    Product request;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // get reference to the views
        tvIsConnected = (TextView) findViewById(R.id.tvIsConnected);
        etName = (EditText) findViewById(R.id.searchText);
        btnPost = (Button) findViewById(R.id.searchButton);

        // check if you are connected or not
        if(isConnected()){
            tvIsConnected.setBackgroundColor(0xFF00CC00);
            tvIsConnected.setText("THE GENIE IS LISTENING....");
        }
        else{
            tvIsConnected.setText("You are NOT connected to the net");
        }

        // add click listener to Button "POST"
        btnPost.setOnClickListener(this);

    }

    public static String POST(String url, Product request){
        InputStream inputStream = null;
        String result = "";
        try {

            // 1. create HttpClient
            HttpClient httpclient = new DefaultHttpClient();

            // 2. make POST request to the given URL
            HttpPost httpPost = new HttpPost(url);

            String json = "";

            // 3. build jsonObject
            JSONObject jsonObject = new JSONObject();
            jsonObject.accumulate("request", request.getSearchString());

            // 4. convert JSONObject to JSON to String
            json = jsonObject.toString();
            Log.d("Json: ", "> " + json);

            // 5. set json to StringEntity
            StringEntity se = new StringEntity(json);

            // 6. set httpPost Entity
            httpPost.setEntity(se);

            // 7. Set some headers to inform server about the type of the content
            httpPost.setHeader("Accept", "application/json");
            httpPost.setHeader("Content-type", "application/json");

            // 8. Execute POST request to the given URL
            HttpResponse httpResponse = httpclient.execute(httpPost);

            // 9. receive response as inputStream
            inputStream = httpResponse.getEntity().getContent();

            // 10. convert inputstream to string
            if(inputStream != null) {
                result = convertInputStreamToString(inputStream);
                Log.d("ResponseMainActivity: ", "> " + result);
            }
            else
                result = "Did not work!";

        } catch (Exception e) {
            Log.d("InputStream", e.getLocalizedMessage());
        }
        Log.d("ResponseMainActivity: ", "> " + result);

        // 11. return result
        return result;
    }

    public boolean isConnected(){
        ConnectivityManager connMgr = (ConnectivityManager) getSystemService(Activity.CONNECTIVITY_SERVICE);
        NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
        if (networkInfo != null && networkInfo.isConnected())
            return true;
        else
            return false;
    }
    @Override
    public void onClick(View view) {

        switch(view.getId()) {
            case R.id.searchButton:
                if (!validate()) {
                    Toast.makeText(getBaseContext(), "Enter some data!", Toast.LENGTH_LONG).show();
                } else {

                    // call AsynTask to perform network operation on separate thread
                    new HttpAsyncTask().execute("http://26fc60dd.ngrok.com/post");
                    break;
                }
        }
    }
    private class HttpAsyncTask extends AsyncTask<String, Void, String> {

        @Override
        protected void onPreExecute() {

            super.onPreExecute();
        }

        @Override
        protected String doInBackground(String... urls) {
            request = new Product();
            request.setSearchString(etName.getText().toString());

            return POST(urls[0],request);
        }
        // onPostExecute displays the results of the AsyncTask.
        @Override
        protected void onPostExecute(String result) {

            Toast.makeText(getBaseContext(), "Result!!!", Toast.LENGTH_LONG).show();
            etName.setText("");
            Intent in = new Intent(getApplicationContext(),ResultActivity.class);
            in.putExtra(TAG_RESULT,result);
            startActivity(in);
        }
    }

    private boolean validate(){
        if(etName.getText().toString().trim().equals(""))
            return false;
        else
            return true;
    }
    private static String convertInputStreamToString(InputStream inputStream) throws IOException {
        BufferedReader bufferedReader = new BufferedReader( new InputStreamReader(inputStream));
        String line = "";
        String result = "";
        while((line = bufferedReader.readLine()) != null)
            result += line;

        inputStream.close();
        return result;

    }
}