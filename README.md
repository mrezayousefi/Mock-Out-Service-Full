# Mock OUT Service - تست سرویس‌های بیرونی با WireMock و Docker Compose

این پروژه برای تست سرویس‌های بیرونی بدون اتصال به سیستم اصلی طراحی شده است.
با استفاده از **Docker Compose** و **WireMock** می‌توانید سرویس‌ها را شبیه‌سازی کنید.

## ساختار پروژه
```
mock-out-service/
├─ docker-compose.yml
├─ mocks/
│   └─ card-issue.json
```

## راه‌اندازی
```bash
git clone https://github.com/mrezayousefi/Mock-Out-Service-Full.git
cd Mock-Out-Service-Full
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
