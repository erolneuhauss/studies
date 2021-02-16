FROM registry.fritz.box/my/arm64v8/ubuntu
RUN apt update && apt install -y curl

#CMD ["curl","-vI","cluster.fritz.box"]
ENTRYPOINT ["curl"]
CMD ["-vI","registry.fritz.box"]
