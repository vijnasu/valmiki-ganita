import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    "depth (km)": [
        "0-1", "1-3", "3-5", "5-10", "10-15", "15-20", "20-25", "25-30", "30-35", "35-40", 
        "40-45", "45-50", "50-55", "55-60", "60-65", "65-70", "70-75", "75-80", "80-85", 
        "85-90", "90-95", "95-100", "100-110", "110-120", "120-130", "130-140", "140-150", 
        "150-160", "160-170", "170-180", "180-190", "190-200", "200-220", "220-240", 
        "240-260", "260-280", "280-300", "300-320"
    ],
    "group": [
        "Surface Metals", 
        "Shallow Earth Alloys", 
        "Crustal Iron Group", 
        "Deep Crust Silicates", 
        "Basaltic Composites", 
        "Granite Layer Metals", 
        "Sedimentary Copper Group", 
        "Metamorphic Blends", 
        "Lower Crust Ferrites", 
        "Sub-crustal Nickelates", 
        "Upper Mantle Cobaltites", 
        "Mantle Platinum Group", 
        "Transitional Gold Series", 
        "Molybdenum Deep Layer", 
        "Lithospheric Chromium Group", 
        "Tectonic Palladium Series", 
        "Basal Layer Aluminates", 
        "Mantle Boundary Titanium Group", 
        "Upper Mantle Magnesites", 
        "Deep Mantle Zirconates", 
        "Lower Mantle Vanadates", 
        "Mantle-Crust Uranites", 
        "Seismic Wave Thorites", 
        "Lithosphere-asthenosphere Bismuthides", 
        "Asthenosphere Silver Group", 
        "Tectonic Fracture Zincates", 
        "Deep Transition Strontium Class", 
        "Upper Mantle Iodides", 
        "Mantle Flow Antimonides", 
        "Convection Current Tellurides", 
        "Deep Mantle Sulfides", 
        "Mantle Plume Carbonates", 
        "Sub-asthenosphere Nitrates", 
        "Asthenospheric Borates", 
        "Lower Mantle Fluorides", 
        "Deep Mantle Chlorides", 
        "Mantle-Crust Boundary Phosphides", 
        "Basal Mantle Argentates"
    ],
    "description": [
        "Commonly found near the Earth's surface. Includes metals like iron, copper, and aluminum, often extracted through open-pit mining.", 
        "Metals like zinc and lead, found in shallow underground mines, often associated with volcanic activity.", 
        "Deeper iron deposits, requiring advanced mining techniques. These irons are denser and purer.", 
        "Metals combined with silicon, forming various silicate minerals. Used in high-strength alloys.", 
        "Metals found in basalt rock layers, including nickel and magnesium, used in strong, corrosion-resistant alloys.", 
        "Trace metals like lithium, found in granite formations. Important for electronic applications.", 
        "Deep-seated copper deposits, often with traces of gold and silver, used in electrical components.", 
        "Rare metals found in metamorphic rocks, including tantalum and niobium, crucial for electronics.", 
        "Iron combined with rare earth elements, producing strong permanent magnets.", 
        "Deep nickel reserves, often associated with volcanic magma sources.", 
        "Cobalt-rich metals, essential for high-performance alloys and batteries.", 
        "Platinum and related metals, important for catalysis and electronics.", 
        "Deep gold deposits, often in quartz veins, used in various high-tech applications.", 
        "Essential for steel alloys, found in deeper rock formations.", 
        "Chromium deposits for stainless steel and other superalloys.", 
        "Palladium, primarily used in catalytic converters, found near tectonic boundaries.", 
        "High-pressure aluminum variants, used in aerospace and engineering.", 
        "Titanium reserves found near the mantle-crust interface, crucial for aerospace and medical applications.", 
        "Magnesium-rich deposits, used in lightweight alloys.", 
        "Zirconium metals, essential in nuclear reactors and strong alloys.", 
        "Vanadium for high-strength steel and energy storage systems.", 
        "Uranium deposits for nuclear fuel, found at extreme depths.", 
        "Thorium, potentially used for nuclear energy, located in seismically active zones.", 
        "Bismuth, used in fire detection and extinguishing systems.", 
        "Deep-seated silver deposits, used in electronics and jewelry.", 
        "Zinc, found in areas with tectonic activity, used for galvanization and alloys.", 
        "Strontium, used in electronics and pyrotechnics, found in deep transition zones.", 
        "Iodine, essential for medical and nutritional applications.", 
        "Antimony, used in flame retardants and batteries.", 
        "Tellurium, important for solar panels and thermoelectric devices.", 
        "Sulfur-rich ores, used in chemical industries and acid production.", 
        "Calcium carbonate, found in mantle plumes, used in construction and agriculture.", 
        "Nitrate minerals, key for fertilizers and explosives.", 
        "Boron, crucial for glass and ceramics, found in the asthenosphere.", 
        "Fluorine, used in refrigerants and pharmaceuticals.", 
        "Chlorine for water treatment and PVC production.", 
        "Phosphorus, essential for agriculture and detergents.", 
        "Deep argentum (silver) deposits, with potential for high conductivity applications."
],

# Sanskrit names for the groups
"sanskrit_iso_names" : [
    "Pr̥thvītala Dhātu Samūhaḥ", 
    "Uparibhūmi Miśradhātu Samūhaḥ", 
    "Bhūparpa Ayassamūhaḥ",
    "Gahanapr̥thvī Saikata Samūhaḥ", 
    "Basaltika Saṃyojanāḥ", 
    "Granthitaśilā Dhātu Samūhaḥ",
    "Avasādī Tāmra Samūhaḥ", 
    "Rūpāntarita Miśraṇa Samūhaḥ", 
    "Adhobhūparpa Lohaka Samūhaḥ", 
    "Upaparpa Rūpaka Samūhaḥ", 
    "Uccāvaraṇa Ketvātu Samūhaḥ", 
    "Āvaraṇa Mahātu Samūhaḥ", 
    "Saṅkramaṇīya Svarṇa Śreṇī", 
    "Gahanaparta Saṃvarṇātu Talam", 
    "Bhūparpa Varṇātu Samūhaḥ", 
    "Bhūgarbhika Nicūṣātu Śreṇī", 
    "Mūlatala Sphaṭayātu Samūhaḥ", 
    "Āvaraṇasīmā Rañjātu Samūhaḥ", 
    "Uccāvaraṇa Bhrājātu Samūhaḥ", 
    "Gahanāvaraṇa Gomedātu Samūhaḥ", 
    "Adhoāvaraṇa Rocātu Samūhaḥ", 
    "Āvaraṇabhūparpa Mīḍhātu Samūhaḥ", 
    "Bhūkampataraṅga Praijātu Samūhaḥ", 
    "Bhūparpāsthenosphera Bhidātu Samūhaḥ",
    "Asthenosphera Rajata Samūhaḥ", 
    "Bhūgarbhaviccheda Kupyātu Samūhaḥ", 
    "Gahanasaṅkramaṇa Śoṇātu Vargaḥ",
    "Uccāvaraṇa Jambukī Samūhaḥ", 
    "Āvaraṇapravāha Añjana Samūhaḥ", 
    "Saṃvahanadhārā Vaṅgaka Samūhaḥ",
    "Gahanāvaraṇa Gandhaka Samūhaḥ", 
    "Āvaraṇasrotas Cūrṇātu Samūhaḥ", 
    "Adhoasthenosphera Bhūyātu Samūhaḥ",
    "Asthenosphera Ṭāṅkaṇa Samūhaḥ", 
    "Adhoāvaraṇa Tarasvinī Samūhaḥ", 
    "Gahanāvaraṇa Nīrajī Samūhaḥ",
    "Āvaraṇabhūparpa Bhāsvara Samūhaḥ", 
    "Mūlāvaraṇa Rajata Samūhaḥ"
],

# Sanskrit names for the groups
"sanskrit_devanagari_names" : [
    "पृथ्वीतल धातु समूहः", 
    "उपरिभूमि मिश्रधातु समूहः", 
    "भूपर्प अयस्समूहः", 
    "गहनपृथ्वी सैकत समूहः", 
    "बसल्तिक संयोजनाः", 
    "ग्रन्थितशिला धातु समूहः", 
    "अवसादी ताम्र समूहः", 
    "रूपांतरित मिश्रण समूहः",  
    "अधोभूपर्प लोहक समूहः", 
    "उपपर्प रूपक समूहः", 
    "उच्चावरण केत्वातु समूहः", 
    "आवरण महातु समूहः", 
    "संक्रमणीय स्वर्ण श्रेणी", 
    "गहनपर्त संवर्णातु तलम्", 
    "भूपर्प वर्णातु समूहः", 
    "भूगर्भिक निचूषातु श्रेणी", 
    "मूलतल स्फटयातु समूहः", 
    "आवरणसीमा रञ्जातु समूहः", 
    "उच्चावरण भ्राजातु समूहः", 
    "गहनावरण गोमेदातु समूहः", 
    "अधोआवरण रोचातु समूहः", 
    "आवरणभूपर्प मीढातु समूहः", 
    "भूकम्पतरंग प्रैजातु समूहः", 
    "भूपर्पास्थेनोस्फेर भिदातु समूहः", 
    "अस्थेनोस्फेर रजत समूहः", 
    "भूगर्भविच्छेद कुप्यातु समूहः", 
    "गहनसंक्रमण शोणातु वर्गः", 
    "उच्चावरण जम्बुकी समूहः", 
    "आवरणप्रवाह अञ्जन समूहः", 
    "संवहनधारा वङ्गक समूहः", 
    "गहनावरण गन्धक समूहः", 
    "आवरणस्रोतस् चूर्णातु समूहः", 
    "अधोअस्थेनोस्फेर भूयातु समूहः", 
    "अस्थेनोस्फेर टाङ्कण समूहः", 
    "अधोआवरण तरस्विनी समूहः", 
    "गहनावरण नीरजी समूहः",
    "आवरणभूपर्प भास्वर समूहः", 
    "मूलावरण रजत समूहः"
],

# Additional descriptions and notes
"additional_descriptions" : [
    "Includes metals like iron, copper, and aluminum, found in the uppermost layer of the Earth's crust.",
    "Zinc, lead, and tin, which are often mined from shallow underground mines.",
    "Deep iron deposits, accessible through advanced mining techniques.",
    "Metals like magnesium and nickel, often found in ultramafic and mafic rocks.",
    "Metals associated with basaltic magma, such as copper and gold.",
    "Rare metals like lithium, beryllium, and tantalum, found in pegmatite deposits within granite.",
    "Not applicable, as sedimentary mining doesn't occur at these depths.",
    "Not applicable, as mining at these depths is not feasible.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining.",
    "Not accessible for mining."
 ]
}
# Merge all the data into a dataframe
df = pd.DataFrame({
    "Depth Range (km)": data["depth (km)"],
    "Element Group": data["group"],
    "Description": data["description"],
    "Sanskrit Devanagari Name": data["sanskrit_devanagari_names"],
    "Sanskrit ISO Name": data["sanskrit_iso_names"],
    "Additional Notes": data["additional_descriptions"]
})

# Export the dataframe to an Excel file
file_path = 'Element_Groups_Depths.xlsx'
#df.to_excel(file_path, index=False)

print(file_path)

# Open the saved Excel file
df = pd.read_excel('Element_Groups_Depths.xlsx')

# Create a figure with a specific size
plt.figure(figsize=(10, 8))

# Plotting each group with its respective depth
for i, group in enumerate(df["Sanskrit ISO Name"]):
    # Extract the depth range and parse it for numeric value
    depth_range = df["Depth Range (km)"][i]
    depth_values = depth_range.split('-')
    avg_depth = (float(depth_values[0]) + float(depth_values[-1])) / 2  # Calculate average depth for each range

    plt.barh(group, avg_depth, align='center', color='skyblue', edgecolor='black')

# Set labels and title
plt.xlabel('Average Depth (km)')
plt.ylabel('Sanskrit ISO Names')
plt.title('Groups of Elements with Respective Depths in the Earth\'s Crust')

# Invert y-axis to show surface at the top
plt.gca().invert_yaxis()

# Show grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adjust layout to fit the window
plt.tight_layout()

# Show the graph
plt.show()

# Save the plot as a file
plt.savefig('alloy_sanskrit_iso_plot.png', dpi=600)
