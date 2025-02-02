from fastapi import FastAPI

app = FastAPI(
    swagger_ui_parameters={
    },
    title="odc-fastapi-api",
)


# TODO
#  по /docs тоже можно и нужно красоту навести. См.: https://dev.to/amal/replacing-fastapis-default-api-docs-with-elements-391d


