package com.textmining.wishmatcher04;

import android.app.ListActivity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;

public class ResultActivity extends ListActivity {

    private ProgressDialog pDialog;

    private static final String TAG_PRODUCT = "product";
    private static final String TAG_URL = "url";
    private static final String TAG_RESULT = "result";

    ArrayList<HashMap<String, String>> contactList;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);

        contactList = new ArrayList<HashMap<String, String>>();

        ListView lv = getListView();

        // Listview on item click listener
        lv.setOnItemClickListener(new OnItemClickListener() {

            @Override
            public void onItemClick(AdapterView<?> parent, View view,
                                    int position, long id) {
                // getting values from selected ListItem
                String product = ((TextView) view.findViewById(R.id.name)).getText().toString();
                String url = ((TextView) view.findViewById(R.id.url)).getText().toString();

                // Starting single contact activity
                Intent in = new Intent(getApplicationContext(),SingleContactActivity.class);
                in.putExtra(TAG_PRODUCT, product);
                in.putExtra(TAG_URL, url);
                startActivity(in);

            }

        });

        // Calling async task to get json
        new GetContacts().execute();
    }
    /**
     * Async task class to get json by making HTTP call
     * */
    private class GetContacts extends AsyncTask<Void, Void, Void> {

        @Override
        protected void onPreExecute() {
            super.onPreExecute();
            // Showing progress dialog
            pDialog = new ProgressDialog(ResultActivity.this);
            pDialog.setMessage("Please wait...");
            pDialog.setCancelable(false);
            pDialog.show();

        }

        @Override
        protected Void doInBackground(Void... arg0) {

            String jsonStr = getIntent().getExtras().getString("result");

            Log.d("Response: ", "> " + jsonStr);

            if (jsonStr != null) {
                try {
                    JSONArray jsonArray = new JSONArray(jsonStr);

                    // looping through All Contacts
                    for (int i = 0; i < jsonArray.length(); i++) {
                        JSONObject c = jsonArray.getJSONObject(i);
                        String product = c.getString(TAG_PRODUCT);
                        String url = c.getString(TAG_URL);

                        // tmp hashmap for single contact
                        HashMap<String, String> contact = new HashMap<String, String>();

                        // adding each child node to HashMap key => value
                        contact.put(TAG_PRODUCT, product);
                        contact.put(TAG_URL, url);

                        // adding contact to contact list
                        contactList.add(contact);

                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            } else {
                Log.e("ServiceHandler", "Couldn't get any data from the url");
            }

            return null;
        }

        @Override
        protected void onPostExecute(Void result) {
            super.onPostExecute(result);
            // Dismiss the progress dialog
            if (pDialog.isShowing())
                pDialog.dismiss();
            /**
             * Updating parsed JSON data into ListView
             * */
            ListAdapter adapter = new SimpleAdapter(
                    ResultActivity.this, contactList,
                    R.layout.activity_list_item, new String[] { TAG_PRODUCT, TAG_URL }, new int[] { R.id.name, R.id.url});

            setListAdapter(adapter);
        }

    }

}


