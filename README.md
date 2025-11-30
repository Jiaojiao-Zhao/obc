# 🥢 Discover Kunshan · 昆山美食文化互动地图
### Interactive Cultural Food Map · INFO301 Final Project

**Authors:** Weisheng Zhang, Jiaojiao Zhao  
**Live Demo:** https://jiaojiao-zhao.github.io/Info301-Final-Project/front.html  

Discover Kunshan is an **interactive geospatial storytelling tool** that maps the everyday culinary landscape of Kunshan.  
It highlights **local eateries, cultural narratives, and neighborhood identities** through an accessible browser-based interface.

Built entirely with **Python + Folium**, the project integrates custom HTML/CSS popups, field photographs, and narrative annotations, and is deployed via **GitHub Pages**.


## ✨ Key Features

- 📍 **Interactive food map** with zoom, hover preview, and full cultural story cards  
- 🍜 **Cuisine category filters** and **affordability indicators**  
- 🖼️ **Base64-embedded photos** ensuring stable cross-browser loading  
- 🗺️ **Narrative geospatial design** — each location is a “story node,” not just a marker  
- 🚶 **Micro food-walk routes** showing thematic sequences across neighborhoods  
- 🌐 **Fully static deployment** with no backend requirements  


## 🗺️ Visualization

👉 **Open the interactive map:**  
https://jiaojiao-zhao.github.io/Info301-Final-Project/front.html

The visualization includes:
- Restaurant markers  
- Cultural description cards  
- Field photos  
- Neighborhood-based food patterns  


## 🛠️ Technical Workflow

### **1. Data Processing (Python)**
- Clean & validate field-collected geospatial data  
- Standardize cuisine types, price levels, and metadata  
- Convert photos to Base64 for embedding  
- Output structured inputs for Folium  

### **2. Prototyping (Plotly)**
- Visual layout exploration  
- Color encoding experiments  
- Narrative density evaluation  

### **3. Map Construction (Folium)**
- Basemap rendering (Stadia Maps + OSM)  
- Restaurant marker placement  
- Custom HTML/CSS popup card generation  
- Filter-based interaction  

### **4. Deployment**
- Export standalone HTML file  
- Deploy via GitHub Pages  


## 📚 Interdisciplinary Foundations

This project draws from:
- **Information Visualization:** narrative design patterns, annotations, audience framing  
- **Digital Humanities:** interpreting everyday food culture through spatial stories  
- **Anthropology & Museum Studies:** restaurants as cultural artifacts  
- **Data Ethics:** transparency, inclusivity, careful contextual representation  

These ideas shaped our design of story cards, thematic food-walk routing, and community-centered framing.


## 🌍 UN SDG Contributions

| Goal | Contribution |
|------|--------------|
| **SDG 4 – Quality Education** | Cultural learning through food stories |
| **SDG 8 – Decent Work & Economic Growth** | Visibility for small independent eateries |
| **SDG 11 – Sustainable Cities & Communities** | Community-rooted, accessible urban storytelling |
| **SDG 17 – Partnerships for the Goals** | Open-source documentation & fieldwork collaboration |


## 📁 Repository Structure

```plaintext
Info301-Final-Project/
│
├── pictures/                   # Base64 source photos
├── README.md
├── app.py                      # Main map for resturants information
├── front.html                  # Main entry for the interactive map
├── index.html                  # Github showcase format
└── suzhou_cultural_map.html    # Output of app.py link to the front page
>>>>>>> 456b380 (update)
