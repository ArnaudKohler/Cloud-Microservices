package org.acme;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import jakarta.json.JsonObject;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import java.time.LocalDateTime;

import org.acme.database.MariaDBService;

import io.smallrye.mutiny.Uni;

@Path("/log")
@ApplicationScoped
public class LogService {

    private static final String RESULT_KEY = "result";

    @Inject
    MariaDBService mariaDBService;

    @POST
    @Produces(MediaType.TEXT_PLAIN)
    public Uni<String> log(JsonObject body) {
        String currentTime = LocalDateTime.now().toString();
        try {
            String bodyString = body.getString(RESULT_KEY);
            String log = currentTime + " - " + bodyString;
            mariaDBService.inserIntoDB(bodyString, currentTime);
            return Uni.createFrom().item(log);
        }
        catch (Exception e) {
            return Uni.createFrom().item("Body does not contain a 'result' key");
        }
    }

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    @Path("/get")
    public Uni<String> get() {

        return mariaDBService.getLog();
    }
}
