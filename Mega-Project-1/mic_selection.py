import speech_recognition as sr
import time

def test_all_microphones():
    """Test each microphone to find the best one"""
    r = sr.Recognizer()
    test_phrase = "hello computer"
    
    print("🎯 Testing all microphones. Say 'hello computer' clearly.")
    print("-" * 50)
    
    for i in range(len(sr.Microphone.list_microphone_names())):
        try:
            name = sr.Microphone.list_microphone_names()[i]
            print(f"\nTesting #{i}: {name[:50]}...")
            
            with sr.Microphone(device_index=i) as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print(f"Say '{test_phrase}' now...")
                audio = r.listen(source, timeout=3, phrase_time_limit=5)
                
                try:
                    text = r.recognize_google(audio)
                    print(f"✅ Heard: {text}")
                    if test_phrase in text.lower():
                        print(f"🎉 PERFECT! Use device_index={i}")
                        return i
                except:
                    print("❌ Didn't hear correctly")
                    
        except Exception as e:
            print(f"❌ Failed: {str(e)[:50]}")
    
    print("\n🔍 Testing complete. Using default microphone.")
    return None

# Run the test
best_mic = test_all_microphones()
if best_mic is not None:
    print(f"\n✨ Best microphone found! Update your code to use:")
    print(f"   device_index={best_mic}")