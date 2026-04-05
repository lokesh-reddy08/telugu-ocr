# Telugu Wikisource Contribution Guide 📚
## Build Real Open-Source Experience for OKI

This guide will help you make **real contributions** to Telugu digital preservation.

---

## 🚀 Quick Start (15 minutes to first contribution!)

### Step 1: Create Account
1. Go to: **https://te.wikisource.org**
2. Click **"ఖాతా సృష్టించు"** (Create Account) in top right
3. Suggested username: `LokeshReddy08` or similar
4. Verify email

### Step 2: Find Pages to Proofread

**Beginner-Friendly Books:**

| Book | Type | Link |
|------|------|------|
| ఆంధ్రుల చరిత్ర | History | https://te.wikisource.org/wiki/ఆంధ్రుల_చరిత్ర |
| వేమన పద్యాలు | Poetry | https://te.wikisource.org/wiki/వేమన_పద్యాలు |

**Direct Proofreading Links:**
- https://te.wikisource.org/wiki/Special:IndexPages (All available books)
- Look for pages marked **red** (not proofread) or **yellow** (needs validation)

### Step 3: Proofread a Page

1. Click on any book index
2. Find a page number marked red/yellow
3. You'll see:
   - **Left side**: Scanned image of original page
   - **Right side**: OCR-generated text (often has errors!)
4. **Your job**: Compare and fix errors
5. Click **"Save"** with edit summary like: "Proofreading - fixed OCR errors"

---

## 🎯 Common OCR Errors to Fix

| OCR Output | Correct Telugu |
|------------|----------------|
| ం (missing) | Add proper anusvara |
| Similar-looking characters | న/ణ, ల/ళ, శ/స |
| Word spacing | Fix merged/split words |
| Missing vowel marks | Add proper gunintalu |

---

## 📝 Track Your Contributions

After proofreading, note your stats:

```
Username: _______________
Pages Proofread: ___
Books Contributed To: ___
Start Date: ___
```

**View your contributions:**
https://te.wikisource.org/wiki/Special:Contributions/YOUR_USERNAME

---

## 💼 For Your Resume

After 5-10 pages, you can write:

> **Open Source Contributor** | Telugu Wikisource
> - Proofread XX pages of digitized Telugu literature
> - Corrected OCR errors in historical texts
> - Contributed to digital preservation of Telugu heritage
> - Username: [link to contributions page]

---

## 🔧 Using Your OCR Tool with Wikisource

You can use your `telugu-ocr` project to:

1. **Download scanned pages** from Wikisource
2. **Run your OCR** to compare with existing text
3. **Identify errors** using confidence scores
4. **Fix them** on Wikisource

```python
# Example workflow
from ocr_telugu import extract_with_confidence

result = extract_with_confidence('wikisource_page.png')

# Find words that might have OCR errors
for word in result['words']:
    if word['confidence'] < 70:
        print(f"⚠️ Check: {word['word']}")
```

---

## 📱 Tips for Effective Proofreading

1. **Start small** - Do 1-2 pages to understand the workflow
2. **Use Telugu keyboard** - Install Google Input Tools or Windows Telugu keyboard
3. **Be consistent** - Even 1 page/day builds a track record
4. **Join the community** - Telugu Wikisource has helpful editors

---

## 🏆 Contribution Goals

| Level | Pages | Resume Value |
|-------|-------|--------------|
| Beginner | 5 pages | "Contributed to Telugu Wikisource" |
| Intermediate | 20 pages | "Active contributor with XX edits" |
| Advanced | 50+ pages | "Significant contributor to Telugu digital preservation" |

---

Good luck with your contributions! 🎉

*Guide created for OKI-IIIT Hyderabad internship preparation*
