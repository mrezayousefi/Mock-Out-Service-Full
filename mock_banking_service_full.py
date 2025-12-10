mock-banking-service/
├─ docker-compose.yml
├─ README.md
├─ mocks/
│   └─ card-issue.json
└─ .gitignore

---

# docker-compose.yml
version: "3.9"
services:
  mock-api:
    image: wiremock/wiremock:latest
    container_name: mock-api
    ports:
      - "8080:8080"
    volumes:
      - ./mocks:/home/wiremock/mappings
    restart: unless-stopped

---

# mocks/card-issue.json
{
  "request": {
    "method": "POST",
    "url": "/card/api/v1/b2b/card/issue",
    "bodyPatterns": [
      { "matchesJsonPath": "$[?(@.serviceType == 'CARD_ISSUE')]" }
    ]
  },
  "response": {
    "status": 200,
    "jsonBody": {
      "traceId": "{{jsonPath request.body '$.traceId'}}",
      "status": "SUCCESS",
      "message": "Card issued successfully"
    },
    "headers": {
      "Content-Type": "application/json"
    }
  }
}

---

# README.md
# Mock Banking Service

این پروژه برای تست سرویس‌های بانکی بدون اتصال به سیستم اصلی طراحی شده است.
با استفاده از **Docker Compose** و **WireMock** می‌توانید سرویس‌ها را شبیه‌سازی کنید.

## ساختار پروژه
```
mock-banking-service/
├─ docker-compose.yml
├─ mocks/
│   └─ card-issue.json
```

## راه‌اندازی
```bash
git clone https://github.com/<your-username>/mock-banking-service.git
cd mock-banking-service
docker-compose up -d
```

## تست سرویس
- **Endpoint:** `POST http://localhost:8080/card/api/v1/b2b/card/issue`
- **Header:** `Content-Type: application/json`
- **Body:** JSON مشابه درخواست اصلی

نمونه پاسخ موفق:
```json
{
  "traceId": "123e4567-e89b-12d3-a456-426614174000",
  "status": "SUCCESS",
  "message": "Card issued successfully"
}
```

## توسعه
- فایل‌های JSON داخل پوشه `mocks/` قابل ویرایش و اضافه کردن سناریوهای جدید هستند.
- هر mapping جدید با Docker Compose بدون تغییر اضافی اجرا می‌شود.

---

# .gitignore
*.log
*.env