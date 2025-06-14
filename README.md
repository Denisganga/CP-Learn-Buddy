# CP Learn Buddy 🧠🎧

**CP Learn Buddy** is an accessible learning tool designed to assist children with Cerebral Palsy (CP) in getting started with reading and learning. By combining the power of Amazon Polly and a simple Flask interface, it converts educational text into clear, human-like speech—empowering impaired learners with audio learning support.

---

## 🚀 What It Does

- Accepts text input from users (e.g., simple educational content like alphabets or reading practice).
- Converts the input into speech using **Amazon Polly**.
- Stores the generated MP3 in **Amazon S3**.
- Returns a public audio link that users can listen to directly.

---

## 🎯 Inspiration

Many children with CP face challenges with traditional reading approaches due to limited mobility and speech difficulties. We wanted to create a simple but powerful tool that could give them a voice and an opportunity to learn through listening. This project was born out of the desire to make education more inclusive using accessible cloud technologies.

---

## 🛠️ Technologies Used

- **Languages**: Python  
- **Frameworks**: Flask  
- **Cloud Services**:  
  - AWS Lambda  
  - Amazon Polly  
  - Amazon S3  
  - Amazon API Gateway  
  - AWS IAM  
  - (Optional) Amazon CloudWatch for logs  
- **Libraries**:  
  - `boto3` (AWS SDK for Python)  
  - `uuid`, `json`

---

## ✅ Accomplishments That We're Proud Of

- Successfully deployed a working audio-learning application using serverless AWS services.
- Integrated TTS (Text-to-Speech) with real-time audio playback.
- Made the tool accessible to learners with CP via a simple, clean UI.

---

## 📚 What We Learned

- How to build and deploy AWS Lambda functions.
- Integrating Amazon Polly and managing access permissions with IAM.
- Storing and serving public assets using S3 buckets.
- Debugging issues like 403, 502, and AccessDenied errors using CloudWatch and permissions policies.

---

## 🔮 What's Next for CP Learn Buddy

- Add support for different languages and regional accents.
- Integrate simple quizzes or interaction-based learning.
- Include image-to-text reading using OCR for visual content.
- Package as a mobile-friendly web app for offline use.

---

## 🧪 Example Input

> "Let's learn the alphabet. A is for Apple, B is for Ball, C is for Cat. Great job! Let's say it again. A, B, C..."

The application will generate an MP3 file and return a link to listen to the spoken version of this content.

---

