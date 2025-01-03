package org.acme.database;

import org.eclipse.microprofile.config.inject.ConfigProperty;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import io.smallrye.mutiny.Multi;
import io.smallrye.mutiny.Uni;
import io.vertx.core.Vertx;
import io.vertx.mutiny.mysqlclient.MySQLPool;
import jakarta.annotation.PostConstruct;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;

@ApplicationScoped
public class MariaDBService {

    static Logger logger = LoggerFactory.getLogger(MariaDBService.class);
    
    @Inject
    Vertx vertx;

    @Inject
    MySQLPool client;

    public void inserIntoDB(String body, String currentTime) {
        String query = "INSERT INTO LogTable (time,calculus) VALUES ('" + currentTime + "', '" + body + "')";
        client.query(query).execute().subscribe().with(
            item -> {
                logger.info("Inserted into DB");
            },
            failure -> {
                logger.error("Failed to insert into DB");
            }
        );
    }

    public Uni<String> getLog() {
        return client.query("SELECT * FROM LogTable").execute()
            .onItem().transformToMulti(rows -> Multi.createFrom().iterable(rows)).onItem().transform(row -> {
                return row.getString("time") + " - " + row.getString("calculus");
            }).collect().asList().onItem().transform(list -> {
                return String.join("\n", list);
            });
    }

}
