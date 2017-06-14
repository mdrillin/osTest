FROM amancevice/superset

USER superset

MAINTAINER Mark Drilling <mdrillin@redhat.com>

ENV SUPERSET_HOME /superset

# admin auth details
ENV ADMIN_USERNAME admin
ENV ADMIN_FIRST_NAME admin
ENV ADMIN_LAST_NAME user
ENV ADMIN_EMAIL admin@nowhere.com
ENV ADMIN_PWD superset

# remove build dependencies
RUN mkdir $SUPERSET_HOME

COPY superset-init.sh /superset-init.sh
RUN chmod +x /superset-init.sh

VOLUME $SUPERSET_HOME

ENTRYPOINT [ "/superset-init.sh" ]

