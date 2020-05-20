## Introduction

The purpose of this test is to show your troubleshooting skills, knowledge of tools required to understand the behaviour of an unknown program and understanding of infrastructure components needed to run a service in a production environment.

## Story

During our migration to the new infrastructure, we have found a legacy system running a single binary.

Unfortunately there is no documentation for the program or source code available. All we could find is a simple help built in the binary:

```
$ ./legacy -h
Usage: legacy <string>
```

Running it with a single argument causes the program to stop after a few seconds printing only "timeout". Value of the argument is not important, but the program won't run without it.

We were told two things about it.

First, that it should respond to HTTP GET request on `/` and `/health` endpoints.

Second, that it can operate in degraded mode in which it returns HTTP status code 202 instead of 200 on all endpoints. Degraded mode doesn't affect users, but we would prefer it fully operational.

## Attachment

[legacy](https://s3.amazonaws.com/cdn.tray.io/static/hr/hiring/tests/legacy)

## Goal

Your goal is to find out why the program "times out" and what to do to fix it. We would also like to know more about it, so please share all your findings and what methods and tools you used in the process.

Next step is to create production infrastructure for the application using a provider and tools of your choice. This should be done in a way that even people without full knowledge of all infrastructure components are able to create/destroy the setup.

## Delivery

Provide a link to a public repository containing:

- Description of your examination process with steps required to understand the working of the legacy program
- Solution used to create infrastructure with clear instructions on using it (if solution is in binary format, source code should be provided as well)

## Evaluation

Please consider the folowing:

- Readability
- Ease of use
- Can it be used in an automated environment (Jenkins, other CI tools)
- Reusability
- Actually solving the problem
