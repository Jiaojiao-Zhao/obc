import folium
from folium.features import DivIcon
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

# Create feature groups for different categories
barbecue_group = folium.FeatureGroup(name='🍖 烧烤烤肉 Barbecue')
seafood_group = folium.FeatureGroup(name='🦀 海鲜 Seafood')
cafe_group = folium.FeatureGroup(name='☕ 咖啡早午餐 Cafe & Brunch')
hotpot_group = folium.FeatureGroup(name='🍲 火锅 Hotpot')
fastfood_group = folium.FeatureGroup(name='🍔 美式快餐 American Fast Food')
local_group = folium.FeatureGroup(name='🍜 地方菜系 Local Food')

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



# Add all feature groups to the map
barbecue_group.add_to(m)
seafood_group.add_to(m)
cafe_group.add_to(m)
hotpot_group.add_to(m)
fastfood_group.add_to(m)
local_group.add_to(m)

# Add layer control as a collapsible button - starts collapsed for cleaner UI
folium.LayerControl(position='topright', collapsed=True).add_to(m)

m.save("suzhou_cultural_map.html")

m
