import os
from bs4 import BeautifulSoup

file_path = r"C:\Users\angam\Downloads\Nexyra Website\Contact\Contact Us Page\contact.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

card_holder = soup.find("div", class_="contact-hero-card-holder")
if card_holder:
    cards = card_holder.find_all("div", class_="contact-hero-card", recursive=False)
    
    if len(cards) >= 3:
        call_us_card = cards[0]
        email_card = cards[1]
        hq_card = cards[2]
        
        # Change phone number
        phone_p = call_us_card.find("p", string="+27 00 000 0000")
        if phone_p:
            phone_p.string = "+27 69 411 5473"
        elif call_us_card.find("p", class_="contact-card-text-02"):
            # Fallback
            call_us_card.find("p", class_="contact-card-text-02").string = "+27 69 411 5473"
            
        # Optional: remove fixed styles if any, or adjust width so it stacks nicely
        call_us_card['style'] = "width: 100%; max-width: 400px;"
        email_card['style'] = "width: 100%; max-width: 400px;"
        
        # Remove HQ card
        hq_card.decompose()
        
        # Create a new container for the vertical stack
        vertical_container = soup.new_tag("div")
        vertical_container['style'] = "display: flex; flex-direction: column; gap: 1.5rem; margin-top: 2.5rem; width: 100%;"
        
        # Move the cards to the new container
        vertical_container.append(call_us_card)
        vertical_container.append(email_card)
        
        # Find the destination
        info_content = soup.find("div", class_="contact-info-text-content")
        if info_content:
            info_content.append(vertical_container)
            
        # Remove the original holder
        card_holder.decompose()

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Contact page updated successfully.")
