/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package redmineManagement;

import java.io.IOException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.json.*;

/**
 *
 * @author user
 */
public class RedmineJournalsReader {

    private String redmineUrl;
    private String apiKey;

    public RedmineJournalsReader(String redmineUrl, String key) {
        this.redmineUrl = redmineUrl;
        this.apiKey = key;
    }

    public ArrayList<String> getJournals(String issueId) {

        OkHttpClient client = new OkHttpClient();

        String requestStr = redmineUrl + "/issues/" + issueId + ".json";

        HttpUrl.Builder urlBuilder = HttpUrl.parse(requestStr).newBuilder();
        urlBuilder.addQueryParameter("include", "journals");

        String url = urlBuilder.build().toString();

        Request request = new Request.Builder()
                .url(url)
                .header("X-Redmine-API-Key", this.apiKey)
                .header("Content-Type", "application/json")
                .build();

        Response response = null;
        String responseStr = "";
        try {
            response = client.newCall(request).execute();
            responseStr = response.body().string();
        } catch (IOException ex) {
            Logger.getLogger(RedmineJournalsReader.class.getName()).log(Level.SEVERE, null, ex);
        }
        ArrayList<String> journal = parseNames(responseStr);
        return journal;
    }

    private ArrayList<String> parseNames(String responseStr) {
        ArrayList<String> journal = new ArrayList<String>();
        try {
            JSONObject obj = null;
            if (!responseStr.toLowerCase().contains("captcha")) {
                obj = new JSONObject(responseStr);
            } else {
                obj = new JSONObject("{" + "" + "}");
            }
            JSONArray arr = obj.getJSONObject("issue").getJSONArray("journals");
            for (int i = 0; i < arr.length(); i++) {
                String name = arr.getJSONObject(i).getJSONObject("user").getString("name");
                journal.add(name);
            }
        } catch (JSONException ex) {
            Logger.getLogger(RedmineJournalsReader.class.getName()).log(Level.SEVERE, null, ex);
        }
        return journal;
    }

    public String getStudentsName(int issueId, String manager) {
        ArrayList<String> allNames = this.getJournals(String.valueOf(issueId));
        if (manager.equals("")){
            manager = "Sergey Politsyn";
        }
        String retVal = manager;
        
        for (int i = 0; i < allNames.size(); i++) {
            if (!allNames.get(i).equals(manager)) {
                retVal = allNames.get(i);
                break;
            }
        }
        return retVal;
    }

    public String getStudentsName(int issueId) {
        return getStudentsName(issueId, "Sergey Politsyn");
    }
}
