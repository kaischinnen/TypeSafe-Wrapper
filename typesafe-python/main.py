import os

import httpx2

from collections.abc import Mapping

from typesafe_sdk import RetryPolicy, TypeSafeClient


class JevLib:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        model: str | None = None,
        retry: RetryPolicy | None = None,
        timeout: float | httpx2.Timeout | None = None,
        headers: Mapping[str, str] | None = None,
        transport: httpx2.BaseTransport | None = None,
        http_client: httpx2.Client | None = None,
        base_url: str | None = None,
    ) -> None:
        self.setup_api_key(api_key)
        self.setup_client(
            model=model,
            retry=retry,
            timeout=timeout,
            headers=headers,
            transport=transport,
            http_client=http_client,
            base_url=base_url,
        )

    def setup_client(
        self,
        *,
        model: str | None = None,
        retry: RetryPolicy | None = None,
        timeout: float | httpx2.Timeout | None = None,
        headers: Mapping[str, str] | None = None,
        transport: httpx2.BaseTransport | None = None,
        http_client: httpx2.Client | None = None,
        base_url: str | None = None,
    ) -> None:
        self.client = TypeSafeClient(
            api_key=self.TYPESAFE_API_KEY,
            model=model,
            retry=retry,
            timeout=timeout,
            headers=headers,
            transport=transport,
            http_client=http_client,
            base_url=base_url,
        )

    def setup_api_key(self, api_key: str | None = None) -> None:
        if api_key is not None:
            self.TYPESAFE_API_KEY = api_key
            return

        try:
            self.TYPESAFE_API_KEY = os.environ["TYPESAFE_API_KEY"]
        except KeyError:
            raise RuntimeError("Missing required environment variable: $TYPESAFE_API_KEY") from None


def main():
    JevLib()


if __name__ == "__main__":
    main()
                 
