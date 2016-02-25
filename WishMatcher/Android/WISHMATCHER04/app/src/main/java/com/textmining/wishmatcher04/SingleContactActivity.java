package com.textmining.wishmatcher04;

import android.app.Activity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.TextView;

import java.util.List;

public class SingleContactActivity extends Activity
{

    // JSON node keys
    private static final String TAG_NAME = "product";
    private static final String TAG_URL = "url";
    private List<String> contactList;
    private WebView ourBrow;
    TextView tv;
    //private static final String TAG_PHONE_MOBILE = "mobile";
    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_webview);
        tv = (TextView) findViewById(R.id.textView1);
        ourBrow = (WebView) findViewById(R.id.webView1);
        WebSettings websettings = ourBrow.getSettings();
        websettings.setJavaScriptEnabled(true);


        String product = getIntent().getExtras().getString("product");
        String wv = getIntent().getExtras().getString("url");
        //display text
        tv.setText(product);

        ourBrow.loadUrl(String.valueOf(wv));
        ourBrow.setWebViewClient(new WebViewClient());

    }
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        // Check if the key event was the Back button and if there's history
        if ((keyCode == KeyEvent.KEYCODE_BACK) && ourBrow.canGoBack()) {
            ourBrow.goBack();
            return true;
        }
        // If it wasn't the Back key or there's no web page history, bubble up to the default
        // system behavior (probably exit the activity)
        return super.onKeyDown(keyCode, event);
    }

}
