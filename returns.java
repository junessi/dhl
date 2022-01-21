import java.net.*;
import org.json.simple.JSONException;


public class returns
{
    public static void main (String[] args)
    {
        String url="http://url.com";
        URL object=new URL(url);

        HttpURLConnection con = (HttpURLConnection) object.openConnection();
        con.setDoOutput(true);
        con.setDoInput(true);
        con.setRequestProperty("Content-Type", "application/json");
        con.setRequestProperty("Accept", "application/json");
        con.setRequestProperty("Authorization", "Basic Y3JlYXRlRGhsT3JkZXJfMjpYTnBaazl6Ym5pR3Nmd29odlJtVHVOenhXRTNzT0U=");
        con.setRequestProperty("DPDHL-User-Authentication-Token", "Y3JpY2tldGxvbmc6bXlEb3ZhbFBXRDAk");
        con.setRequestMethod("POST");

        JSONObject jsonData = new JSONObject("{}");
        /*
                                           + "    \"receiverId\": \"deu\","
                                           + "    \"customerReference\": \"123456789\","
                                           + "    \"shipmentReference\": \"Sendungsreferenz\","
                                           + "    \"senderAddress\": {"
                                           + "      \"name1\": \"Zhang San\","
                                           + "      \"name2\": \"Li Si\","
                                           + "      \"name3\": \"Wang Wu\","
                                           + "      \"streetName\": \"Vegesacker Heerstr.\","
                                           + "      \"houseNumber\": \"111\","
                                           + "      \"postCode\": \"28757\","
                                           + "      \"city\": \"Bremen\","
                                           + "      \"country\": {"
                                           + "        \"countryISOCode\": \"DEU\","
                                           + "        \"country\": \"Germany\""
                                           + "      }"
                                           + "    },"
                                           + "    \"email\": \"Test.Mustermann@doval.de\","
                                           + "    \"telephoneNumber\": \"+49 351 987654321\","
                                           + "    \"weightInGrams\": 5000,"
                                           + "    \"returnDocumentType\": \"SHIPMENT_LABEL\""
                                           + "  }");
        */
    }
}
