main
[2024-10-28 13:59:15,378] [WARN ] [] [c.c.n.r.i.ReadModelPartitionStarterActor] [akka://NaSystem/system/sharding/paymentReturnBusinessEventsKafka%401.0/3/__NA_ReadModelStarter_paymentReturnBusinessEventsKafka_3/__NA_ReadModelStarter_paymentReturnBusinessEventsKafka] - method=onFailure failed to start read model partition actor: Failure(java.util.concurrent.CompletionException: akka.pattern.AskTimeoutException: Ask timed out on [Actor[akka://NaSystem/system/sharding/paymentReturnBusinessEventsKafka%401.0/3/__NA_ReadModelStarter_paymentReturnBusinessEventsKafka_3/__NA_ReadModelStarter_paymentReturnBusinessEventsKafka/3#185228198]] after [10000 ms]. Message of type [com.clear2pay.na.readmodel.internal.StartUpdatingReadModel]. A typical reason for `AskTimeoutException` is that the recipient actor didn't send a reply.). Retrying...
java.util.concurrent.CompletionException: akka.pattern.AskTimeoutException: Ask timed out on [Actor[akka://NaSystem/system/sharding/paymentReturnBusinessEventsKafka%401.0/3/__NA_ReadModelStarter_paymentReturnBusinessEventsKafka_3/__NA_ReadModelStarter_paymentReturnBusinessEventsKafka/3#185228198]] after [10000 ms]. Message of type [com.clear2pay.na.readmodel.internal.StartUpdatingReadModel]. A typical reason for `AskTimeoutException` is that the recipient actor didn't send a reply.
	at java.base/java.util.concurrent.CompletableFuture.encodeThrowable(CompletableFuture.java:332)
	at java.base/java.util.concurrent.CompletableFuture.completeThrowable(CompletableFuture.java:347)
	at java.base/java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:636)
	at java.base/java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:510)
	at java.base/java.util.concurrent.CompletableFuture.completeExceptionally(CompletableFuture.java:2162)
	at scala.concurrent.java8.FuturesConvertersImpl$CF.apply(FutureConvertersImpl.scala:29)
	at scala.concurrent.java8.FuturesConvertersImpl$CF.apply(FutureConvertersImpl.scala:26)
	at scala.concurrent.impl.Promise$Transformation.run(Promise.scala:484)
	at scala.concurrent.ExecutionContext$parasitic$.execute(ExecutionContext.scala:222)
	at scala.concurrent.impl.Promise$Transformation.submitWithValue(Promise.scala:429)
	at scala.concurrent.impl.Promise$DefaultPromise.submitWithValue(Promise.scala:335)
	at scala.concurrent.impl.Promise$DefaultPromise.tryComplete0(Promise.scala:285)
	at scala.concurrent.impl.Promise$DefaultPromise.tryComplete(Promise.scala:278)
	at akka.pattern.PromiseActorRef$.$anonfun$apply$1(AskSupport.scala:730)
	at akka.actor.Scheduler$$anon$7.run(Scheduler.scala:479)
	at scala.concurrent.ExecutionContext$parasitic$.execute(ExecutionContext.scala:222)
	at akka.actor.LightArrayRevolverScheduler$TaskHolder.executeTask(LightArrayRevolverScheduler.scala:365)
	at akka.actor.LightArrayRevolverScheduler$$anon$3.executeBucket$1(LightArrayRevolverScheduler.scala:314)
	at akka.actor.LightArrayRevolverScheduler$$anon$3.nextTick(LightArrayRevolverScheduler.scala:318)
	at akka.actor.LightArrayRevolverScheduler$$anon$3.run(LightArrayRevolverScheduler.scala:270)
	at java.base/java.lang.Thread.run(Thread.java:833)
Caused by: akka.pattern.AskTimeoutException: Ask timed out on [Actor[akka://NaSystem/system/sharding/paymentReturnBusinessEventsKafka%401.0/3/__NA_ReadModelStarter_paymentReturnBusinessEventsKafka_3/__NA_ReadModelStarter_paymentReturnBusinessEventsKafka/3#185228198]] after [10000 ms]. Message of type [com.clear2pay.na.readmodel.internal.StartUpdatingReadModel]. A typical reason for `AskTimeoutException` is that the recipient actor didn't send a reply.

[2024-10-28 13:51:09,612] [WARN ] [] [c.c.n.r.a.e.AbstractExceptionMapper] [] - REST response computation completed exceptionally response=ExceptionResponse{status=Service Unavailable, entity=ErrorResponse{type='null', title='null', message='Request timed out. Service unavailable.', details=[ErrorResponseDetails{code='UNKNOWN', subcode='null', cause='null', message='Request timed out. Service unavailable.', fields=[]}]}} reason=null
java.util.concurrent.TimeoutException: null

[2024-10-28 13:51:09,612] [WARN ] [] [c.c.n.t.e.i.T.RequestProcessed] [] - Http request user="SVC11649", httpMethod="GET", requestURI="/pom/v1/api/payment/customerCreditTransfers", baseURI="https://gorm-pom-nft01:8445", requestHeaders="{}", requestEntries="{}", statusCode="503", serviceName="customerCreditTransfer.search", responseTime="60020ms", responseMessage="{"details":[{"code":"UNKNOWN","message":"Request timed out. Service unavailable."}]}", contentLength="84", severity="WARN", uuid="2834b114-4d12-4189-89b9-4375e498d9d5", code="RequestProcessed" producer=com.clear2pay.na.rest.server.internal.logging.LoggingFilter

Oct 28, 2024 1:50:23 PM org.glassfish.jersey.server.ServerRuntime$Responder writeResponse
SEVERE: An I/O error has occurred while writing a response message entity to the container output stream.
org.glassfish.jersey.server.internal.process.MappableException: java.io.IOException: Close SendCallback@3f83ad6a[PROCESSING][i=null,cb=org.eclipse.jetty.server.HttpChannel$SendCallback@54cf71c1] in state PROCESSING
	at org.glassfish.jersey.server.internal.MappableExceptionWrapperInterceptor.aroundWriteTo(MappableExceptionWrapperInterceptor.java:67)
	at org.glassfish.jersey.message.internal.WriterInterceptorExecutor.proceed(WriterInterceptorExecutor.java:139)
	at com.clear2pay.na.rest.server.internal.logging.HttpTrafficLoggingFilter.aroundWriteTo(HttpTrafficLoggingFilter.java:195)
	at org.glassfish.jersey.message.internal.WriterInterceptorExecutor.proceed(WriterInterceptorExecutor.java:139)
	at org.glassfish.jersey.message.internal.MessageBodyFactory.writeTo(MessageBodyFactory.java:1116)
	at org.glassfish.jersey.server.ServerRuntime$Responder.writeResponse(ServerRuntime.java:649)
	at org.glassfish.jersey.server.ServerRuntime$Responder.processResponse(ServerRuntime.java:380)
	at org.glassfish.jersey.server.ServerRuntime$Responder.process(ServerRuntime.java:370)
	at org.glassfish.jersey.server.ServerRuntime$AsyncResponder$3.run(ServerRuntime.java:871)
	at org.glassfish.jersey.internal.Errors$1.call(Errors.java:248)
	at org.glassfish.jersey.internal.Errors$1.call(Errors.java:244)
	at org.glassfish.jersey.internal.Errors.process(Errors.java:292)
	at org.glassfish.jersey.internal.Errors.process(Errors.java:274)
	at org.glassfish.jersey.internal.Errors.process(Errors.java:244)
	at org.glassfish.jersey.process.internal.RequestScope.runInScope(RequestScope.java:265)
	at org.glassfish.jersey.server.ServerRuntime$AsyncResponder.resume(ServerRuntime.java:903)
	at org.glassfish.jersey.server.ServerRuntime$AsyncResponder.resume(ServerRuntime.java:859)
	at java.base/java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:646)
	at java.base/java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:510)
	at java.base/java.util.concurrent.CompletableFuture.complete(CompletableFuture.java:2147)
	at scala.concurrent.java8.FuturesConvertersImpl$CF$$anon$1.accept(FutureConvertersImpl.scala:63)
	at scala.concurrent.java8.FuturesConvertersImpl$CF$$anon$1.accept(FutureConvertersImpl.scala:61)
	at java.base/java.util.concurrent.CompletableFuture.uniWhenComplete(CompletableFuture.java:863)
	at java.base/java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(CompletableFuture.java:841)
	at java.base/java.util.concurrent.CompletableFuture$Completion.exec(CompletableFuture.java:483)
	at java.base/java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:373)
	at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1182)
	at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:1655)
	at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1622)
	at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:165)
Caused by: java.io.IOException: Close SendCallback@3f83ad6a[PROCESSING][i=null,cb=org.eclipse.jetty.server.HttpChannel$SendCallback@54cf71c1] in state PROCESSING
	at org.eclipse.jetty.util.IteratingCallback.close(IteratingCallback.java:444)
	at org.eclipse.jetty.server.HttpConnection.onClose(HttpConnection.java:556)
	at org.eclipse.jetty.io.ssl.SslConnection.onClose(SslConnection.java:347)
	at org.eclipse.jetty.io.SelectorManager.connectionClosed(SelectorManager.java:347)
	at org.eclipse.jetty.io.ManagedSelector$DestroyEndPoint.run(ManagedSelector.java:1115)
	at org.eclipse.jetty.util.thread.QueuedThreadPool.runJob(QueuedThreadPool.java:969)
	at org.eclipse.jetty.util.thread.QueuedThreadPool$Runner.doRunJob(QueuedThreadPool.java:1194)
	at org.eclipse.jetty.util.thread.QueuedThreadPool$Runner.run(QueuedThreadPool.java:1149)
	at java.base/java.lang.Thread.run(Thread.java:833)

PAPI
2024-10-28 14:47:23,444 ERROR [qtp908744222-377] c.n.p.p.s.TransactionFIS: API error from POM, getPaymentList; ; Version:2.6.23 Exception:org.springframework.web.client.ResourceAccessException: I/O error on GET request for "https://gorm-pom-nft01:8445/pom/v1/api/payment/customerCreditTransfers": Request timed out: null Errormsg:I/O error on GET request for "https://gorm-pom-nft01:8445/pom/v1/api/payment/customerCreditTransfers": Request timed out: null

KAFKA
[17:19:54.544] [WARN ] [o.apache.kafka.clients.NetworkClient] [] - [AdminClient clientId=GPE-Payment-Capture-Nft01-b1dc7295-0df1-418d-a82d-04f87c2413f1-admin] Connection to node 12 (ap-cl12t.oneadr.net/10.96.139.79:9093) could not be established. Broker may not be available.
[17:19:54.544] [INFO ] [o.a.k.c.a.i.AdminMetadataManager] [] - [AdminClient clientId=GPE-Payment-Capture-Nft01-b1dc7295-0df1-418d-a82d-04f87c2413f1-admin] Metadata update failed
org.apache.kafka.common.errors.TimeoutException: Call(callName=fetchMetadata, deadlineMs=1729876694618, tries=1, nextAllowedTryMs=1729876794644) timed out at 1729876794544 after 1 attempt(s)
Caused by: org.apache.kafka.common.errors.TimeoutException: Timed out waiting for a node assignment. Call: fetchMetadata


