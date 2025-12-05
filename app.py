import folium
from folium.features import DivIcon
from folium.plugins import FeatureGroupSubGroup
import base64
from folium import IFrame

# Initialize map with Stadia Maps for bilingual support
# Get your free API key from: https://client.stadiamaps.com/signup/
STADIA_API_KEY = "d2f41481-0104-482a-8e02-f924979b7d56"  # Replace with your actual API key

suzhou_coords = [31.40374, 120.92504]

# Using Stadia Maps Alidade Smooth - excellent for bilingual/international labels
# Set tiles=None to prevent base layer from appearing in the layer control
m = folium.Map(
    location=suzhou_coords,
    zoom_start=14,
    tiles=None,
    attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>'
)

# Add Stadia Maps as a tile layer without adding it to layer control
folium.TileLayer(
    tiles=f'https://tiles.stadiamaps.com/tiles/alidade_smooth/{{z}}/{{x}}/{{y}}{{r}}.png?api_key={STADIA_API_KEY}',
    attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
    name='Stadia Maps',
    overlay=False,
    control=False  # Don't show in layer control
).add_to(m)

# Create feature groups with two-layer structure
# Layer 1: Main categories (parent groups)
culinary_parent = folium.FeatureGroup(name='🍽️ Culinary 美食', show=True)
cultural_parent = folium.FeatureGroup(name='🏛️ Cultural Sights 文化景点', show=True)

# Layer 2: Subcategories under Culinary (child groups)
barbecue_group = FeatureGroupSubGroup(culinary_parent, name='🍖 烧烤烤肉 Barbecue', show=True)
seafood_group = FeatureGroupSubGroup(culinary_parent, name='🦀 海鲜 Seafood', show=True)
cafe_group = FeatureGroupSubGroup(culinary_parent, name='☕ 咖啡早午餐 Cafe & Brunch', show=True)
hotpot_group = FeatureGroupSubGroup(culinary_parent, name='🍲 火锅 Hotpot', show=True)
fastfood_group = FeatureGroupSubGroup(culinary_parent, name='🍔 美式快餐 American Fast Food', show=True)
local_group = FeatureGroupSubGroup(culinary_parent, name='🍜 地方菜系 Local Food', show=True)

# Cultural sights - using parent group directly (no subcategories)
cultural_group = cultural_parent

site_1 = [31.38896807679732, 120.9220200006602]

with open("pictures/很久以前.png", "rb") as image_file:
    encoded1 = base64.b64encode(image_file.read()).decode('utf-8')

html1 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #fff9f5 0%, #ffe8d6 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(255,107,53,0.1);
    color: #2b2926;
    overflow: hidden;
">
  <!-- Header Image -->
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded1}"
         alt="很久以前烧烤门店"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(255,107,53,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(255,107,53,0.3);
    ">🔥 必吃烧烤</div>
  </div>
  
  <!-- Content -->
  <div style="padding: 24px;">
    <!-- Title Section -->
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        很久以前
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #ff6b35; font-weight: 500;">
        Long Time Ago
      </p>
    </div>
    
    <!-- Rating -->
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #fff3e6, #ffe4cc);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(255,107,53,0.2);
    ">
      <span style="font-size: 13px; color: #8b5a3c; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★★★</span>
    </div>
    
    <!-- Description -->
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #ff6b35;
    ">
      "很久以前"是一家专注于呼伦贝尔羊肉串的烧烤连锁店，以炭火精烤和稳定美味著称。时常客满、广受欢迎，是朋友聚餐和宵夜的热门选择。<br><br>
      <em style="color: #666; font-size: 13px;">"Long Time Ago" specializes in Hulunbuir lamb skewers with charcoal grilling—perfect for group dinners or late-night bites.</em>
    </p>
    
    <!-- Info Grid -->
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #ff6b35;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">昆山万象汇嗨街一层 · 1F, Vanke Mall Hi Street</div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">呼伦贝尔羊肉串 · 烤生蚝</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">¥90</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/k22X9dVtEs4605vA?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=4449&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #ff6b35, #ff8c61);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(255,107,53,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.2s;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe1 = IFrame(html1, width=420, height=600)
popup1 = folium.Popup(iframe1, max_width=2500)

# Styled marker with circular background and shadow
logo_icon = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #ff6b35;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <img src="pictures/long_time_ago_logo.png" 
             style="width: 36px; height: 36px; object-fit: cover; border-radius: 50%;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_1,
    popup=popup1,
    tooltip="很久以前 Long Time Ago",
    icon=logo_icon
).add_to(barbecue_group)

site_2 = [31.413638, 120.894177]

with open("pictures/蟹王府.jpg", "rb") as image_file:
    encoded2 = base64.b64encode(image_file.read()).decode('utf-8')

html2 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #f0f9ff 0%, #dbeafe 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(14,165,233,0.1);
    color: #1e293b;
    overflow: hidden;
">
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded2}"
         alt="蟹王府"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(14,165,233,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(14,165,233,0.3);
    ">⭐ 米其林一星</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        蟹王府
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #0ea5e9; font-weight: 500;">
        King of Crab
      </p>
    </div>
    
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #e0f2fe, #bae6fd);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(14,165,233,0.2);
    ">
      <span style="font-size: 13px; color: #075985; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★☆☆</span>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #0ea5e9;
    ">
      "蟹王府"以一年四季均能吃到大闸蟹闻名，是连续六年获得米其林一星的餐厅。招牌蟹宴风味浓郁、食材扎实，非常适合聚餐或犒劳自己。<br><br>
      <em style="color: #666; font-size: 13px;">Michelin one-star restaurant known for premium hairy crabs available all year round.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #0ea5e9;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">大渔湾 · Dayu Bay Commercial Area</div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">清蒸大闸蟹 · 蟹粉小笼</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">¥198</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/l3OykiFQbnmnmjSp?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=203&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #0ea5e9, #38bdf8);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(14,165,233,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe2 = IFrame(html2, width=420, height=600)
popup2 = folium.Popup(iframe2, max_width=2500)

# Styled marker with circular background and shadow
icon2 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #0ea5e9;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <img src="pictures/xie_wang_fu_logo.png" 
             style="width: 38px; height: auto; object-fit: contain;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_2,
    popup=popup2,
    tooltip="蟹王府 King of Crab",
    icon=icon2
).add_to(seafood_group)

site_3 = [31.388291, 120.942672]

with open("pictures/AMPM_fixed.png", "rb") as image_file:
    encoded3 = base64.b64encode(image_file.read()).decode('utf-8')

html3 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(59,130,246,0.1);
    color: #1e293b;
    overflow: hidden;
">
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded3}"
         alt="AMPM Cafe&Brunch"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(59,130,246,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(59,130,246,0.3);
    ">☕ 咖啡早午餐</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        AMPM Cafe
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #3b82f6; font-weight: 500;">
        Cafe & Brunch
      </p>
    </div>
    
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #dbeafe, #bfdbfe);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(59,130,246,0.2);
    ">
      <span style="font-size: 13px; color: #1e40af; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★★☆</span>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #3b82f6;
    ">
      AMPM Cafe&Brunch是一家提供全日早午餐和咖啡的休闲餐厅，氛围轻松惬意。晚上有乐队表演，让用餐体验更加丰富。<br><br>
      <em style="color: #666; font-size: 13px;">Cozy all-day brunch spot with live band performances in the evenings.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #3b82f6;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">大西门商业街 · Daximen Commercial Street</div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">松露薯条 · 辣芝士牛肉烤饼</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">¥115</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/l3OykiFQbnmnmjSp?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=203&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #3b82f6, #60a5fa);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(59,130,246,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe3 = IFrame(html3, width=420, height=600)
popup3 = folium.Popup(iframe3, max_width=2500)

# Styled marker with circular background and shadow
icon3 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #3b82f6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <img src="pictures/ampm_logo.jpg" 
             style="width: 36px; height: 36px; object-fit: cover; border-radius: 50%;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_3,
    popup=popup3,
    tooltip="AMPM Cafe&Brunch",
    icon=icon3
).add_to(cafe_group)

site_4 = [31.407038, 120.952177]

with open("pictures/海底捞.jpg", "rb") as image_file:
    encoded4 = base64.b64encode(image_file.read()).decode('utf-8')

html4 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(239,68,68,0.1);
    color: #1e293b;
    overflow: hidden;
">
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded4}"
         alt="海底捞"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(239,68,68,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(239,68,68,0.3);
    ">🍲 火锅 HOTPOT</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        海底捞
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #ef4444; font-weight: 500;">
        Haidilao Hotpot
      </p>
    </div>
    
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #fee2e2, #fecaca);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(239,68,68,0.2);
    ">
      <span style="font-size: 13px; color: #991b1b; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★★★</span>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #ef4444;
    ">
      海底捞以贴心服务与稳定品质著称，是中国最受欢迎的火锅品牌之一。无论是深夜宵夜、好友聚餐还是生日庆祝，都能享受到超高服务体验。<br><br>
      <em style="color: #666; font-size: 13px;">Known nationwide for consistent hotpot quality and exceptional service—perfect for gatherings and late-night dining.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #ef4444;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">招商花园城 5 层 · C-Mall 5F</div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">番茄汤底 · 虾滑 · 肥牛 · 捞面</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">¥109</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/l69GiT5ziWpNm79w?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=3023&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #ef4444, #f87171);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(239,68,68,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe4 = IFrame(html4, width=420, height=600)
popup4 = folium.Popup(iframe4, max_width=2500)

# Styled marker with circular background and shadow
icon4 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #ef4444;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <img src="pictures/haidilao_logo.jpg" 
             style="width: 36px; height: 36px; object-fit: cover; border-radius: 50%;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_4,
    popup=popup4,
    tooltip="海底捞 Haidilao Hotpot",
    icon=icon4
).add_to(hotpot_group)

site_5 = [31.404118, 120.904801]

with open("pictures/SHARK_fixed.png", "rb") as image_file:
    encoded5 = base64.b64encode(image_file.read()).decode('utf-8')

html5 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(245,158,11,0.1);
    color: #1e293b;
    overflow: hidden;
">
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded5}"
         alt="SHARKBURGER"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(245,158,11,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(245,158,11,0.3);
    ">🍔 美式快餐</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        SHARKBURGER
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #f59e0b; font-weight: 500;">
        American Fast Food
      </p>
    </div>
    
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(245,158,11,0.2);
    ">
      <span style="font-size: 13px; color: #92400e; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★★☆</span>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #f59e0b;
    ">
      SHARKBURGER专注制作地道美式汉堡，深受当地国际社区群体的喜爱。汉堡肉饼厚实多汁，面包松软，搭配地道非常纯正。<br><br>
      <em style="color: #666; font-size: 13px;">Specializes in authentic American-style burgers—a favorite among the local international community.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">昆山人才专墅 · Kunshan Talent Apartment</div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">经典美式牛肉堡</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">¥60</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/l3OykiFQbnmnmjSp?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=203&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #f59e0b, #fbbf24);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(245,158,11,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe5 = IFrame(html5, width=420, height=600)
popup5 = folium.Popup(iframe5, max_width=2500)

# Styled marker with circular background and shadow
icon5 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #f59e0b;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <img src="pictures/shark_logo.jpg" 
             style="width: 36px; height: 36px; object-fit: cover; border-radius: 50%;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_5,
    popup=popup5,
    tooltip="SHARKBURGER",
    icon=icon5
).add_to(fastfood_group)

site_6 = [31.383045, 120.953025]

with open("pictures/heishu_fixed.png", "rb") as image_file:
    encoded6 = base64.b64encode(image_file.read()).decode('utf-8')

html6 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #fff9f5 0%, #ffe8d6 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(239,68,68,0.1);
    color: #1e293b;
    overflow: hidden;
">
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded6}"
         alt="嘿叔烧烤"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(239,68,68,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(239,68,68,0.3);
    ">🔥 烧烤烤肉</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        嘿叔烧烤
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #ef4444; font-weight: 500;">
        Heishu Barbeque
      </p>
    </div>
    
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #fff3e6, #ffe4cc);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(239,68,68,0.2);
    ">
      <span style="font-size: 13px; color: #8b5a3c; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★★★</span>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #ef4444;
    ">
      嘿叔烧烤是昆山极具人气的深夜食堂，以特色牛肉串和地道风味俘获食客味蕾。肉质鲜嫩，调味到位，环境舒适，晚上有音乐表演。<br><br>
      <em style="color: #666; font-size: 13px;">Popular late-night eatery famous for specialty beef skewers with live music performances.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #ef4444;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">昆山碧乐时光商场 · Kunshan Bileshiguang Shopping Mall</div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">红柳木羔羊后腿串 · 烤法式羊排</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">¥75</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/l3OykiFQbnmnmjSp?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=203&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #ef4444, #f87171);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(239,68,68,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe6 = IFrame(html6, width=420, height=600)
popup6 = folium.Popup(iframe6, max_width=2500)

# Styled marker with circular background and shadow
icon6 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #ef4444;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <img src="pictures/heishu_logo.jpg" 
             style="width: 36px; height: 36px; object-fit: cover; border-radius: 50%;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_6,
    popup=popup6,
    tooltip="嘿叔烧烤 Heishu Barbeque",
    icon=icon6
).add_to(barbecue_group)


site_7 = [31.403675, 120.959179]

with open("pictures/chuwairendejia.png", "rb") as image_file:
    encoded7 = base64.b64encode(image_file.read()).decode('utf-8')

html7 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(59,130,246,0.1);
    color: #1e293b;
    overflow: hidden;
">
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded7}"
         alt="出外人的家"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(59,130,246,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(59,130,246,0.3);
    ">🍜 台湾菜系</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        出外人的家
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #3b82f6; font-weight: 500;">
        Chuwairendejia
      </p>
    </div>
    
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #dbeafe, #bfdbfe);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(59,130,246,0.2);
    ">
      <span style="font-size: 13px; color: #1e40af; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★★☆</span>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #3b82f6;
    ">
      "出外人的家"是昆山一家以台湾菜为主的餐厅，兼顾本地家常菜，适合家庭聚餐或朋友小聚。由台湾同学推荐，具备正宗台湾风味，口味浓郁且分量十足。<br><br>
      <em style="color: #666; font-size: 13px;">Taiwanese-focused restaurant offering authentic flavors with rich and generous portions.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #3b82f6;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">黄河北路保昆商苑D楼 · Huanghe North Road</div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">三杯鸡 · 蚵仔煎</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">¥75</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/l3OykiFQbnmnmjSp?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=203&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #3b82f6, #60a5fa);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(59,130,246,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe7 = IFrame(html7, width=420, height=600)
popup7 = folium.Popup(iframe7, max_width=2500)

# Styled marker with circular background and shadow
icon7 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #3b82f6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <img src="pictures/chuwairendejia_logo.jpg" 
             style="width: 36px; height: 36px; object-fit: cover; border-radius: 50%;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_7,
    popup=popup7,
    tooltip="出外人的家 Chuwairendejia",
    icon=icon7
).add_to(local_group)

site_8 = [31.399960, 120.927540]

with open("pictures/maojia.jpg", "rb") as image_file:
    encoded8 = base64.b64encode(image_file.read()).decode('utf-8')

html8 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(239,68,68,0.1);
    color: #1e293b;
    overflow: hidden;
">
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded8}"
         alt="毛家湘菜馆"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(239,68,68,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(239,68,68,0.3);
    ">🌶️ 湘菜</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        毛家湘菜馆
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #ef4444; font-weight: 500;">
        Maojia Hunan Cuisine
      </p>
    </div>
    
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #ffe4e6, #fecdd3);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(239,68,68,0.2);
    ">
      <span style="font-size: 13px; color: #991b1b; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★★★</span>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #ef4444;
    ">
      毛家湘菜馆是一家以地道湘菜为特色的餐厅，适合家庭聚餐或朋友小聚。提供许多经典湖南风味菜肴，有鲜辣香浓的口味和明档厨房的透明化烹饪。<br><br>
      <em style="color: #666; font-size: 13px;">Authentic Hunan dishes with bold flavors and transparent cooking in the open kitchen.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #ef4444;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">花园路2045号 · 2045 Huayuan Road</div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">剁椒鱼头 · 小炒黄牛肉</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">¥76</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/l69GiT5ziWpNm79w?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=3023&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #ef4444, #f87171);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(239,68,68,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe8 = IFrame(html8, width=420, height=600)
popup8 = folium.Popup(iframe8, max_width=2500)

# Styled marker with circular background and shadow
icon8 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #ef4444;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <img src="pictures/maojia_logo.jpg" 
             style="width: 36px; height: 36px; object-fit: cover; border-radius: 50%;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_8,
    popup=popup8,
    tooltip="毛家湘菜馆 Maojia Hunan Cuisine",
    icon=icon8
).add_to(local_group)


site_9 = [31.415638, 120.945672]


with open("pictures/yuzhanggui.jpg", "rb") as image_file:
    encoded_yz = base64.b64encode(image_file.read()).decode('utf-8')


html_yz = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(37,99,235,0.1);
    color: #1e293b;
    overflow: hidden;
">
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded_yz}"
         alt="渔掌柜酸菜鱼"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(37,99,235,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(37,99,235,0.3);
    ">🐟 酸菜鱼</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        渔掌柜酸菜鱼
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #2563eb; font-weight: 500;">
        Yuzhanggui Sauerkraut Fish
      </p>
    </div>
    
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #dbeafe, #bfdbfe);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(37,99,235,0.2);
    ">
      <span style="font-size: 13px; color: #1d4ed8; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★★☆</span>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #2563eb;
    ">
      昆山本地特色鱼锅店，不吃辣的朋友可以选择番茄锅，非常清爽开胃。<br>
      酸菜鱼也很受欢迎，鱼片细嫩，汤底香浓不腻。<br><br>
      <em style="color: #666; font-size: 13px;">A local Kunshan fish pot restaurant. The tomato broth is perfect for non-spicy eaters. Tender fish slices and a rich, aromatic soup.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #2563eb;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">玉山镇北门路1222号 · Beimen Road No.1222 </div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">番茄鱼 · 酸菜鱼</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">¥66</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/k6boKBjkcO7NA67n?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=4583&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #2563eb, #3b82f6);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(37,99,235,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

# --- 4. Popup IFrame ---
iframe_yz = IFrame(html_yz, width=420, height=600)
popup_yz = folium.Popup(iframe_yz, max_width=2500)

icon_yz = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #2563eb;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <img src="pictures/yuzhanggui_logo.jpg" 
             style="width: 36px; height: 36px; object-fit: cover; border-radius: 50%;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_9,
    popup=popup_yz,
    tooltip="渔掌柜酸菜鱼 Yuzhanggui Sauerkraut Fish",
    icon=icon_yz
).add_to(local_group)

# --- 1. 坐标（你提供的） ---
site_10 = [31.407038, 120.972177]

# --- 2. 加载主图 ---
with open("pictures/mingdong.jpg", "rb") as image_file:
    encoded_md = base64.b64encode(image_file.read()).decode('utf-8')

# --- 3. HTML 卡片内容 ---
html10 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #fff5f5 0%, #fee2e2 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.18), 0 0 0 1px rgba(220,38,38,0.1);
    color: #1e293b;
    overflow: hidden;
">
  <div style="position: relative; overflow: hidden; border-radius: 20px 20px 0 0;">
    <img src="data:image/png;base64,{encoded_md}"
         alt="明洞火炉"
         style="width: 100%; height: 200px; object-fit: cover; display: block;" />
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(220,38,38,0.95);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(220,38,38,0.35);
    ">🔥 Barbecue</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        明洞火炉 · 韩国烤肉
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #dc2626; font-weight: 500;">
        Myeongdong Korean BBQ
      </p>
    </div>
    
    <div style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #fecaca, #fca5a5);
        padding: 8px 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(220,38,38,0.2);
    ">
      <span style="font-size: 13px; color: #b91c1c; font-weight: 600; margin-right: 8px;">推荐指数</span>
      <span style="font-size: 16px; color: #f59e0b;">★★★★☆</span>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #dc2626;
    ">
      好吃种类多的韩国烤肉料理，氛围轻松，适合朋友聚会和非正式小型聚餐。肉质优质，配菜丰富，炭火香气浓郁。<br><br>
      <em style="color: #666; font-size: 13px;">A Korean BBQ place offering a wide variety of meats, casual atmosphere, great for informal gatherings.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #dc2626;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">长江北路中楠都汇广场3号楼6号 · North Changjiang Road, Zhongnan Duhui Plaza, No.6, Building 3 </div>
      </div>
      
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">🍴 Must-Try</div>
        <div style="font-size: 13px; color: #333;">牛排肉 · 牛仔骨</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <div style="
            flex: 1;
            background: white;
            padding: 12px;
            border-radius: 10px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
          <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">💰 Price</div>
          <div style="font-size: 16px; color: #333; font-weight: 700;">100</div>
        </div>
        
        <a href="https://m.dianping.com/shopinfo/lasfOcaKJxzbAXwU?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=114&cityid=416&isoversea=0" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #dc2626, #f87171);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(220,38,38,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>📱 大众点评</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

# --- 4. Popup & IFrame ---
iframe10 = IFrame(html10, width=420, height=600)
popup10 = folium.Popup(iframe10, max_width=2500)

# --- 5. Logo 标记（圆形） ---
icon10 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #dc2626;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    ">
        <img src="pictures/mingdong_logo.jpg" 
             style="width: 36px; height: 36px; object-fit: cover; border-radius: 50%;">
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

# --- 6. 添加到地图 ---
folium.Marker(
    location=site_10,
    popup=popup10,
    tooltip="明洞火炉 Myeongdong Korean BBQ",
    icon=icon10
).add_to(barbecue_group)

# ========== CULTURAL SIGHTS SECTION ==========

# Site 11: Zhouzhuang Mystery of Life Museum 周庄生命奥秘博物馆
site_11 = [31.122222, 120.846472]  # Zhouzhuang area coordinates

# NOTE: Add image file 'pictures/zhouzhuang_museum.jpg' for this site
# For now using a placeholder - replace with actual image
try:
    with open("pictures/zhouzhuang_museum.jpg", "rb") as image_file:
        encoded_11 = base64.b64encode(image_file.read()).decode('utf-8')
except FileNotFoundError:
    # Create a simple colored placeholder if image doesn't exist
    encoded_11 = ""

html11 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(6,182,212,0.1);
    color: #1e293b;
    overflow: hidden;
">
  {"<div style='position: relative; overflow: hidden; border-radius: 20px 20px 0 0;'><img src='data:image/png;base64," + encoded_11 + "' alt='周庄生命奥秘博物馆' style='width: 100%; height: 200px; object-fit: cover; display: block;' />" if encoded_11 else "<div style='height: 200px; background: linear-gradient(135deg, #06b6d4, #0891b2); display: flex; align-items: center; justify-content: center; color: white; font-size: 18px; font-weight: 600;'>周庄生命奥秘博物馆</div>"}
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(6,182,212,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(6,182,212,0.3);
    ">🏛️ 文化景点</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        周庄生命奥秘博物馆
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #06b6d4; font-weight: 500;">
        Zhouzhuang Mystery of Life Museum
      </p>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #06b6d4;
    ">
      周庄生命奥秘博物馆是一座独特的科学展览馆，展示了生物塑化标本和人体科学知识。通过先进的生物塑化技术，展示了各种动物和人体的真实结构，是了解生命科学的绝佳场所。<br><br>
      <em style="color: #666; font-size: 13px;">A unique science museum showcasing bio-plastinated specimens and human anatomy. An excellent place to explore life sciences through advanced preservation technology.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #06b6d4;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">周庄古镇全福路 · Quanfu Road, Zhouzhuang Ancient Town</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <a href="https://surl.amap.com/5dILWY01uL73" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #06b6d4, #0891b2);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(6,182,212,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>🗺️ 高德地图</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe11 = IFrame(html11, width=420, height=520)
popup11 = folium.Popup(iframe11, max_width=2500)

icon11 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #06b6d4;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    ">
        🏛️
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_11,
    popup=popup11,
    tooltip="周庄生命奥秘博物馆 Zhouzhuang Mystery of Life Museum",
    icon=icon11
).add_to(cultural_group)

# Site 12: Tinglin Park 亭林园
site_12 = [31.391981, 120.947420]  # Tinglin Park, Kunshan

try:
    with open("pictures/tinglin_park.jpg", "rb") as image_file:
        encoded_12 = base64.b64encode(image_file.read()).decode('utf-8')
except FileNotFoundError:
    encoded_12 = ""

html12 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(34,197,94,0.1);
    color: #1e293b;
    overflow: hidden;
">
  {"<div style='position: relative; overflow: hidden; border-radius: 20px 20px 0 0;'><img src='data:image/png;base64," + encoded_12 + "' alt='亭林园' style='width: 100%; height: 200px; object-fit: cover; display: block;' />" if encoded_12 else "<div style='height: 200px; background: linear-gradient(135deg, #22c55e, #16a34a); display: flex; align-items: center; justify-content: center; color: white; font-size: 18px; font-weight: 600;'>亭林园</div>"}
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(34,197,94,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(34,197,94,0.3);
    ">🌳 文化景点</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        亭林园
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #22c55e; font-weight: 500;">
        Tinglin Park
      </p>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #22c55e;
    ">
      亭林园是昆山市内最大的综合性公园，以玉峰山（俗称马鞍山）为中心。园内有顾炎武纪念馆、昆曲博物馆等文化景点，风景秀丽，是市民休闲和了解昆山历史文化的好去处。<br><br>
      <em style="color: #666; font-size: 13px;">Kunshan's largest comprehensive park centered around Yufeng Mountain. Features cultural sites including Gu Yanwu Memorial Hall and Kunqu Opera Museum—a great place to explore local history and culture.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #22c55e;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">昆山市马鞍山东路1号 · No.1 Ma'anshan East Road, Kunshan</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <a href="https://surl.amap.com/jVi1dGR15gEI" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #22c55e, #16a34a);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(34,197,94,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>🗺️ 高德地图</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe12 = IFrame(html12, width=420, height=520)
popup12 = folium.Popup(iframe12, max_width=2500)

icon12 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #22c55e;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    ">
        🌳
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_12,
    popup=popup12,
    tooltip="亭林园 Tinglin Park",
    icon=icon12
).add_to(cultural_group)

# Site 13: Zhengyi Ancient Town 正仪古镇
site_13 = [31.373554, 120.857910]  # Zhengyi Ancient Town

try:
    with open("pictures/zhengyi_town.jpg", "rb") as image_file:
        encoded_13 = base64.b64encode(image_file.read()).decode('utf-8')
except FileNotFoundError:
    encoded_13 = ""

html13 = f"""
<div style="
    font-family: 'Noto Sans SC', 'Helvetica Neue', Arial, sans-serif;
    max-width: 380px;
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    border-radius: 20px;
    padding: 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(245,158,11,0.1);
    color: #1e293b;
    overflow: hidden;
">
  {"<div style='position: relative; overflow: hidden; border-radius: 20px 20px 0 0;'><img src='data:image/png;base64," + encoded_13 + "' alt='正仪古镇' style='width: 100%; height: 200px; object-fit: cover; display: block;' />" if encoded_13 else "<div style='height: 200px; background: linear-gradient(135deg, #f59e0b, #d97706); display: flex; align-items: center; justify-content: center; color: white; font-size: 18px; font-weight: 600;'>正仪古镇</div>"}
    <div style="
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(245,158,11,0.95);
        backdrop-filter: blur(10px);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(245,158,11,0.3);
    ">🏘️ 文化景点</div>
  </div>
  
  <div style="padding: 24px;">
    <div style="margin-bottom: 16px;">
      <h3 style="margin: 0; font-size: 24px; font-weight: 700; color: #1a1a1a; line-height: 1.2;">
        正仪古镇
      </h3>
      <p style="margin: 4px 0 0; font-size: 15px; color: #f59e0b; font-weight: 500;">
        Zhengyi Ancient Town
      </p>
    </div>
    
    <p style="
        margin: 0 0 20px;
        font-size: 14px;
        line-height: 1.8;
        color: #4a4a4a;
        background: rgba(255,255,255,0.6);
        padding: 14px;
        border-radius: 12px;
        border-left: 3px solid #f59e0b;
    ">
      正仪古镇有着千年历史，保留了江南水乡的传统风貌。古镇内有古桥、古街、古宅，是体验昆山传统文化和江南水乡风情的理想之地。相比周庄等知名古镇，这里更加宁静古朴。<br><br>
      <em style="color: #666; font-size: 13px;">A thousand-year-old ancient town preserving traditional Jiangnan watertown charm. With ancient bridges, streets, and residences, it offers a quieter, more authentic experience than famous tourist towns.</em>
    </p>
    
    <div style="display: grid; gap: 12px;">
      <div style="
          background: white;
          padding: 12px;
          border-radius: 10px;
          border-left: 3px solid #f59e0b;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      ">
        <div style="font-size: 11px; color: #999; text-transform: uppercase; margin-bottom: 4px;">📍 Location</div>
        <div style="font-size: 13px; color: #333; font-weight: 500;">昆山市巴城镇正仪街道 · Zhengyi Street, Bacheng Town, Kunshan</div>
      </div>
      
      <div style="display: flex; gap: 12px;">
        <a href="https://surl.amap.com/jRad91P15bnH" 
           target="_blank" 
           style="
            flex: 1;
            background: linear-gradient(135deg, #f59e0b, #d97706);
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            text-align: center;
            font-weight: 600;
            font-size: 13px;
            box-shadow: 0 4px 12px rgba(245,158,11,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        ">
          <span>🗺️ 高德地图</span>
        </a>
      </div>
    </div>
  </div>
</div>
"""

iframe13 = IFrame(html13, width=420, height=520)
popup13 = folium.Popup(iframe13, max_width=2500)

icon13 = DivIcon(html=f'''
    <div style="
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: white;
        border: 3px solid #f59e0b;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    ">
        🏘️
    </div>
''', icon_size=(48, 48), icon_anchor=(24, 24))

folium.Marker(
    location=site_13,
    popup=popup13,
    tooltip="正仪古镇 Zhengyi Ancient Town",
    icon=icon13
).add_to(cultural_group)


# Add all feature groups to the map in hierarchical order
# Add Cultural Sights first (so it appears at top)
cultural_parent.add_to(m)

# Then add Culinary parent
culinary_parent.add_to(m)

# Then add Culinary subgroups (they will appear right after Culinary parent)
barbecue_group.add_to(m)
seafood_group.add_to(m)
cafe_group.add_to(m)
hotpot_group.add_to(m)
fastfood_group.add_to(m)
local_group.add_to(m)

# Add layer control as a collapsible button - starts collapsed for cleaner UI
folium.LayerControl(position='topright', collapsed=False).add_to(m)

# Add custom CSS and JavaScript to improve layer control hierarchy display
custom_css_js = """
<style>
/* Style for parent layer groups */
.leaflet-control-layers-overlays label {
    font-weight: normal;
    padding: 2px 5px;
    cursor: pointer;
}

/* Parent group styling */
.parent-group {
    font-weight: bold !important;
    background: rgba(100, 150, 250, 0.15) !important;
    border-radius: 4px;
    padding: 6px 8px !important;
    margin: 3px 0 !important;
    border-left: 4px solid #6495ED;
}

/* Child group styling */
.child-group {
    margin-left: 25px !important;
    font-size: 0.90em;
    padding: 4px 6px !important;
    border-left: 2px solid #ccc;
    margin-top: 1px !important;
    margin-bottom: 1px !important;
    background: rgba(240, 240, 240, 0.3);
    border-radius: 3px;
    transition: all 0.2s ease;
}

/* Hidden state for children */
.child-group.hidden {
    display: none !important;
    opacity: 0;
    max-height: 0;
    overflow: hidden;
}

/* Toggle indicator */
.parent-group::before {
    content: '▼ ';
    font-size: 0.8em;
    margin-right: 5px;
    transition: transform 0.2s;
}

.parent-group.collapsed::before {
    content: '▶ ';
}
</style>

<script>
// Wait for the map to load
setTimeout(function() {
    var overlaysContainer = document.querySelector('.leaflet-control-layers-overlays');
    if (!overlaysContainer) return;
    
    var labels = overlaysContainer.querySelectorAll('label');
    
    // Identify parent and child labels based on text content
    var culinaryParent = null;
    var culturalParent = null;
    var childKeywords = ['Barbecue', 'Seafood', 'Cafe', 'Hotpot', 'American Fast Food', 'Local Food'];
    
    // First pass: identify parents
    labels.forEach(function(label, index) {
        var text = label.textContent || label.innerText;
        
        if (text.includes('Culinary 美食')) {
            label.classList.add('parent-group');
            label.classList.add('collapsed');  // Start collapsed
            label.setAttribute('data-parent', 'culinary');
            culinaryParent = label;
        } else if (text.includes('Cultural Sights 文化景点')) {
            label.classList.add('parent-group');
            label.setAttribute('data-parent', 'cultural');
            culturalParent = label;
        }
    });
    
    // Second pass: identify children based on keywords
    labels.forEach(function(label) {
        var text = label.textContent || label.innerText;
        
        // Check if this label contains any child keywords
        var isChild = childKeywords.some(function(keyword) {
            return text.includes(keyword);
        });
        
        if (isChild) {
            label.classList.add('child-group');
            label.classList.add('hidden');  // Start hidden
            label.setAttribute('data-parent', 'culinary');
        }
    });
    
    // Add click handlers to parent groups
    labels.forEach(function(label) {
        if (label.classList.contains('parent-group')) {
            var parentType = label.getAttribute('data-parent');
            
            // Click handler for toggle
            label.addEventListener('click', function(e) {
                // Only toggle on label click, not checkbox click
                if (e.target.type !== 'checkbox') {
                    e.preventDefault();
                    var isCurrentlyCollapsed = this.classList.contains('collapsed');
                    
                    if (isCurrentlyCollapsed) {
                        // Expand: remove collapsed, show children
                        this.classList.remove('collapsed');
                        showChildren(parentType);
                    } else {
                        // Collapse: add collapsed, hide children
                        this.classList.add('collapsed');
                        hideChildren(parentType);
                    }
                }
            });
        }
    });
    
    function showChildren(parentType) {
        labels.forEach(function(label) {
            if (label.classList.contains('child-group') && label.getAttribute('data-parent') === parentType) {
                label.classList.remove('hidden');
            }
        });
    }
    
    function hideChildren(parentType) {
        labels.forEach(function(label) {
            if (label.classList.contains('child-group') && label.getAttribute('data-parent') === parentType) {
                label.classList.add('hidden');
            }
        });
    }
    
}, 1000);
</script>
"""

m.get_root().html.add_child(folium.Element(custom_css_js))

m.save("suzhou_cultural_map.html")

m
