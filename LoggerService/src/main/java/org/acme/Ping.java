package org.acme;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;

@ApplicationScoped
public class Ping {
    
    @GET
    @Path("/ping")
    public String ping() {
        return "pong";
    }
}
