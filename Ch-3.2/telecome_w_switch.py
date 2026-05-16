print("===== Welcome to Telecom Customer Care =====")
print("Press 1 for English")
print("Press 2 for Hindi")
print("Press 3 for Gujarati")

lang_choice = input("\nSelect your language (1-3): ")

match lang_choice:
    case "1":
        print("\n--- English Service Menu ---")
        print("\nPress 1 for Internet and Data Plans")
        print("Press 2 for Billing and Recharge Queries")
        print("Press 3 to Speak with an Executive")
        press = input("\nEnter your choice: ")
        
        match press:
            case "1":
                print("\nConnecting to Internet and Data Support in English...")
            case "2":
                print("\nOpening Billing and Recharge Services in English...")
            case "3":
                print("\nPlease hold while we connect you to our English Customer Executive...")
            case _:
                print("\nInvalid choice. Call disconnected.")
                
    case "2":
        print("\n--- हिंदी सेवा मेनू (Hindi Service Menu) ---")
        print("\nइंटरनेट और डेटा प्लान के लिए 1 दबाएं")
        print("बिलिंग और रिचार्ज प्रश्नों के लिए 2 दबाएं")
        print("ग्राहक सेवा अधिकारी से बात करने के लिए 3 दबाएं")
        press = input("\nअपना विकल्प चुनें: ")
        
        match press:
            case "1":
                print("\nडेटा और इंटरनेट सहायता टीम से जोड़ा जा रहा है...")
            case "2":
                print("\nबिलिंग और रिचार्ज विभाग में आपका स्वागत है...")
            case "3":
                print("\nकृपया प्रतीक्षा करें, हम आपकी कॉल हमारे हिंदी ग्राहक सेवा अधिकारी को स्थानांतरित कर रहे हैं...")
            case _:
                print("\nअमान्य विकल्प। कॉल समाप्त।")
                
    case "3":
        print("\n--- ગુજરાતી સેવા મેનુ (Gujarati Service Menu) ---")
        print("\nઇન્ટરનેટ અને ડેટા પ્લાન માટે 1 દબાવો")
        print("બિલિંગ અને રિચાર્જ પૂછપરછ માટે 2 દબાવો")
        print("ગ્રાહક સેવા અધિકારી સાથે વાત કરવા માટે 3 દબાવો")
        press = input("\nતમારો વિકલ્પ પસંદ કરો: ")
        
        match press:
            case "1":
                print("\nઇન્ટરનેટ અને ડેટા સપોર્ટ ટીમ સાથે જોડાણ થઈ રહ્યું છે...")
            case "2":
                print("\nબિલિંગ અને રિચાર્જ સેવાઓ ખુલી રહી છે...")
            case "3":
                print("\nકૃપા કરીને રાહ જુઓ, અમે આપનો કૉલ ગુજરાતી ગ્રાહક સેવા અધિકારીને ટ્રાન્સફર કરી રહ્યા છીએ...")
            case _:
                print("\nઅમાન્ય વિકલ્પ. કૉલ સમાપ્ત.")
                
    case _:
        print("Invalid input. Please try calling again and select a valid language option.")