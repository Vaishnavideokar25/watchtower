import os
import firebase_admin
from firebase_admin import credentials

if not firebase_admin._apps:
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": os.environ["watchtower-backend"],
        "private_key": os.environ["-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDIOo4H9xs7VgOg\nNx6THARECHhucG6slkLxyb67kxxQVCaWEoo6gHUhAlRTYXPBTSCHbfG8e0cJg4bu\nWKksUBnlU6MloIeQLxvUdtaARUUMNRLA+U8xl3fZ7boCkWCRacO+gP2lZhaMrvmF\nl/YXxHlnEF3wLFhmjjvOxgcxHjm3ACemztI+sFv3viG6TzSAAVfOOBEO/izDM7G9\n9uNxYJMqznzY36RfW/yV10sVPIh9guWukzRlyOUe8bJs6UuwwSjtsVHSZuPFOutj\nN+P9hRDE9Ag8MJoYVof90sLJ/RkHM7yRxSkkH7/zSUTCm3lUUuqilbHOv6rT3n/B\nfhCEcci3AgMBAAECggEAFJoLGCBhnGrUElg+3JsS3fR907syIAQ78h3fHUoHLUVj\nTP4DsVObTvYAOti5l3zkk8VeYerQmywoe34C4MItz+3u85r/Uni5D9TZwDagYp+p\nWigCG9OpFh1tjgBq+RCdU+IjdwZjMT7QV2G/L/XcGfHSAI7HhRHYby+VTi/9Ieot\na9KhEzSUKyMRtjBglrBpgYiYVgiZmiqQMKdBbYd82Ybjka/Z6gHCejJDr2ntgDqP\nbu+F3DQfVgL/7rgvCcpktoRvGBH2ampXymPaKyQai+W7lhIvrApS2nuGIaAywv2k\nzEvDpaRDfaeIIAT3a4zMDT2ZIO9e8e4W2ytLkEXyuQKBgQD+i12ITn2RwSGRottn\nF6/nZOG8LzAuNoMPiDJ75oTivlRd6WqWE8MkgylR43ww061XjcR/qUF5lQYWxiWG\nNHZUdrrV5tEfrf0A/n7jG6gFPiuu/VBByMh2MK8H1Z07KJbL07tDQUWGx4kGKNj6\nybSiqk/4bxLbwukvpBCUG/CfiQKBgQDJX6zb2RDhPkCbNJLvbWfC1YtipoGXnJwY\nEybwGIGizn+PCo985A/H2Emc4JKrEK8D5MzUBE0f0fBK2t3MgoihI+kD4HWV3HT2\nYZ+G8oT8ZC4eeLlDmvIt48CDL4Kr7tVwe2cLs8RyG58fZ5YcJMBtHDTNpTtp8wwf\n/3sP4m7WPwKBgEDG6qiTgPUktww+66LSrlsumxuuzo4UJUpAmMhbI5ooYYP8sLk8\nkj6qektynto2JDjRxR3Pzu/H8uK8zjPXCf34sRdaRAHR3z7vhQ76rMmYxrkjkdcL\n56fcP864l+jELYv1eARnifAAu2gr4PwBdMyolu1cJupyMbGECQwICDYxAoGAQ9qU\nQYQz9uHmHSYq+LhxxSn1jKk0c6TWyBnz/eUUEYrpWoahcODcHGfZ7h2R7khx4KsB\nBdPpNPaltGNpZ1b4uOuDwcWpeXTOiJK+kVc4zl7nV2cwbgJQ5nuey9V/f3W7v+ok\n/8F0SUrbZFagMx2DJYDingS2L24xQLryeZi/5jsCgYEA1ybV9EcQavFDEiPn/kz0\npEL1biFVjst3EMXl0Lz456xY9WDN1UFDYb3ya8s+p1K224sdeXFzjkEPAXTcb617\nutiEmg7qatwcvAvYp6uiLE0/HKi7z7MVjZpvwegHw6HiTkbBSdm4Ug2gPxqvx8b4\ne+3VOcJOdKGDkR1kX/6Dhkg=\n-----END PRIVATE KEY-----\n"].replace("\\n", "\n"),
        "client_email": os.environ["firebase-adminsdk-fbsvc@watchtower-backend.iam.gserviceaccount.com"],
        "token_uri": "https://oauth2.googleapis.com/token"
    })
    firebase_admin.initialize_app(cred)
