import java.net.*;
import org.json.simple.JSONObject;
import java.io.IOException;
import java.io.OutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class returns
{
    public static void main (String[] args)
    {
        try {
            String url="https://cig.dhl.de/services/production/rest/returns/";
            URL object=new URL(url);

            HttpURLConnection con = (HttpURLConnection)object.openConnection();
            con.setDoOutput(true);
            con.setDoInput(true);
            con.setRequestProperty("Content-Type", "application/json");
            con.setRequestProperty("Accept", "application/json");
            con.setRequestProperty("Authorization", "Basic Y3JlYXRlRGhsT3JkZXJfMjpYTnBaazl6Ym5pR3Nmd29odlJtVHVOenhXRTNzT0U=");
            con.setRequestProperty("DPDHL-User-Authentication-Token", "Y3JpY2tldGxvbmc6bXlEb3ZhbFBXRDAk");
            con.setRequestMethod("POST");

            /*
             * build this json object with JSONObject
            {
                "receiverId": "deu",
                "customerReference": "123456789",
                "shipmentReference": "Sendungsreferenz",
                "senderAddress": {"
                  "name1": "Zhang San",
                  "name2": "Li Si",
                  "name3": "Wang Wu",
                  "streetName": "Vegesacker Heerstr.",
                  "houseNumber": "111",
                  "postCode": "28757",
                  "city": "Bremen",
                  "country": {"
                    "countryISOCode": "DEU",
                    "country": "Germany""
                  }"
                },
                "email": "Test.Mustermann@doval.de",
                "telephoneNumber": "+49 351 987654321",
                "weightInGrams": 5000,
                "returnDocumentType": "SHIPMENT_LABEL"
            }
            */
            JSONObject data = new JSONObject();

            data.put("receiverId", "deu");
            data.put("customerReference", "123456789");
            data.put("shipmentReference", "Sendungsreferenz");

            JSONObject senderAddr = new JSONObject();
            senderAddr.put("name1", "Zhang San");
            senderAddr.put("name2", "Li Si");
            senderAddr.put("name3", "Wang Wu");
            senderAddr.put("streetName", "Vegesacker Heerstr.");
            senderAddr.put("houseNumber", "111");
            senderAddr.put("postCode", "28757");
            senderAddr.put("city", "Bremen");

            JSONObject country = new JSONObject();
            country.put("countryISOCode", "DEU");
            country.put("country", "Germany");
            senderAddr.put("country", country);

            data.put("senderAddress", senderAddr);

            data.put("email", "Test.Mustermann@doval.de");
            data.put("telephoneNumber", "+49 351 987654321");
            data.put("weightInGrams", 5000);
            data.put("returnDocumentType", "SHIPMENT_LABEL");

            OutputStream os = con.getOutputStream();
            os.write(data.toString().getBytes("UTF-8"));
            os.close();

            // display response
            StringBuilder sb = new StringBuilder();
            int HttpResult = con.getResponseCode();
            System.out.println(HttpResult);

            BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream(), "utf-8"));
            String line = null;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
            br.close();

            con.disconnect();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (ProtocolException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
