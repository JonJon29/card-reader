package yes.etazeta;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {

    public static void main(String[] args)
    {
        writeJSON("yes.json");
    }

    public static void writeJSON(String filename)
    {
        try
        {
            JSONObject sampleObject = new JSONObject();
            JSONObject historyObject = new JSONObject();

            JSONArray personen = new JSONArray();
            JSONArray history = new JSONArray();

            personen.add(history);
            history.add("yes");

            sampleObject.put("personen", personen);
            historyObject.put("history", history);

            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            JsonElement je = JsonParser.parseString(sampleObject.toJSONString());
            String prettyJsonString = gson.toJson(je);
            Files.write(Paths.get(filename), prettyJsonString.getBytes());
        }
        catch(IOException exc)
        {
            exc.printStackTrace();
        }
    }
}
