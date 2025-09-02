import tkinter as tk
from tkinter import ttk, messagebox

class DaloRestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dalo Restaurant Menu")
        self.root.geometry("900x700")
        self.root.configure(bg="#f5f5f5")
        
        self.create_header()
        self.create_main_area()
        self.create_footer()
        
        self.load_menu_data()
        
        self.show_main_menu()
    
    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#d32f2f", height=80)
        header_frame.pack(fill="x", padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="Dalo Restaurant", font=("Arial", 24, "bold"), 
                              fg="white", bg="#d32f2f")
        title_label.pack(expand=True)
        
        tagline_label = tk.Label(header_frame, text="Authentic Nepali Cuisine", font=("Arial", 12), 
                                fg="white", bg="#d32f2f")
        tagline_label.pack(expand=True)
    
    def create_main_area(self):
        self.main_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.canvas = tk.Canvas(self.main_frame, bg="#f5f5f5")
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f5f5f5")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        self.canvas.bind("<Enter>", self._bind_mousewheel)
        self.canvas.bind("<Leave>", self._unbind_mousewheel)
    
    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
    
    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def create_footer(self):
        footer_frame = tk.Frame(self.root, bg="#333333", height=50)
        footer_frame.pack(fill="x", padx=10, pady=10)
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(footer_frame, text="TAKE A SEAT, GRAB A TREAT & ENJOY YOUR MEAL!", 
                               font=("Arial", 10), fg="white", bg="#333333")
        footer_label.pack(expand=True)
        
        back_button = tk.Button(footer_frame, text="Back to Main Menu", command=self.show_main_menu,
                               bg="#d32f2f", fg="white", font=("Arial", 10, "bold"))
        back_button.pack(side="right", padx=10)
    
    def load_menu_data(self):
        self.menu_data = {
            "Breakfast": {
                "Boiled Eggs": {"price": "100", "description": "Perfectly cooked fresh farm eggs, served soft, medium, or hard-boiled to your preference. A simple, protein-rich, and healthy choice to start your morning right. 🥚✨"},
                "Omelette (Plain, Cheese, Masala)": {"price": "100/150/200", "description": "Fluffy, golden omelette made with fresh farm eggs. Choose from classic plain, rich and creamy cheese, or spiced masala for a flavorful kick. A hearty breakfast favorite served hot and fresh. 🥚🧀🌿"},
                "Sandwich (Veg, Club, Chicken)": {"price": "200/300/350", "description": "Freshly made sandwiches layered with garden-fresh vegetables, or go classic with a hearty club, or enjoy a protein-packed chicken filling. Perfectly toasted and served with a touch of freshness. 🥪✨"},
                "Toast (Plain, Butter)": {"price": "75/100", "description": "Golden slices of bread, lightly toasted for a crisp bite. Served plain or with a spread of creamy butter for a simple, comforting breakfast choice. 🍞✨"},
                "Sausage (Fry/Boil)": {"price": "300", "description": "Juicy and flavorful sausages, served either perfectly fried for a crispy bite or gently boiled for a lighter option. A classic choice to complete your breakfast plate. 🌭✨"},
                "Saute Mushroom": {"price": "300", "description": "Fresh button mushrooms lightly sautéed with butter, garlic, and herbs for a savory and wholesome side dish. 🍄✨"}
            },
            "Boiled Items": {
                "Paneer and Vegetable": {"price": "400", "description": "Fresh paneer and seasonal vegetables, boiled to perfection. A light and nutritious option, ideal for a healthy meal. 🥦✨"},
                "Sweet Corn": {"price": "300", "description": "Sweet corn kernels, boiled and lightly seasoned. A simple yet delightful snack or side dish, packed with natural sweetness. 🌽✨"},
                "Mutton": {"price": "350", "description": "Tender mutton pieces, boiled to retain their natural flavors. A hearty and protein-rich choice for meat lovers. 🍖✨"},
                "Chicken": {"price": "450", "description": "Juicy chicken pieces, boiled to perfection. A versatile option that can be enjoyed on its own or added to other dishes. 🍗✨"},
                "Sausage": {"price": "300", "description": "Flavorful sausages, boiled for a juicy and tender bite. A classic choice that pairs well with various sides. 🌭✨"}
            },
            "Soups": {
                "Mutton Bone Soup": {"price": "250", "description": "A hearty mutton bone soup, simmered to perfection with spices and herbs. Rich in flavor and perfect for a comforting meal. 🍲✨"},
                "Sweet Corn Soup": {"price": "300", "description": "A delightful sweet corn soup, creamy and flavorful. Perfect as a starter or a light meal, packed with the natural sweetness of corn. 🌽✨"},
                "Hot and Sour Soup": {"price": "250", "description": "A classic hot and sour soup, bursting with flavors. A perfect balance of heat and tanginess, ideal for warming up on a chilly day. 🌶️✨"},
                "Chicken Soup": {"price": "300", "description": "A comforting chicken soup, made with tender chicken pieces and aromatic spices. Perfect for a light meal or as a soothing remedy. 🍗✨"},
                "Mushroom Soup": {"price": "250", "description": "A creamy mushroom soup, rich in flavor and perfect as a starter or a light meal. Made with fresh mushrooms for an earthy taste. 🍄✨"},
                "Mix Veg Soup": {"price": "300", "description": "A mix veg soup, packed with a variety of fresh vegetables. Light and nutritious, perfect for a healthy start to your meal. 🥦✨"}
            },
            "Veg Main Course": {
                "Paneer Butter Masala": {"price": "450", "description": "Creamy and rich paneer butter masala, made with tender paneer cubes simmered in a buttery tomato gravy. Perfectly paired with naan or rice. 🧀✨"},
                "Paneer Tikka Masala": {"price": "450", "description": "Paneer tikka masala, a flavorful dish with marinated paneer cubes cooked in a spicy and tangy gravy. A delightful vegetarian option that is sure to please. 🧀✨"},
                "Mix Veg Curry": {"price": "300", "description": "A hearty mix veg curry, packed with a variety of fresh vegetables cooked in a rich and flavorful gravy. A wholesome dish that is perfect for any meal. 🥦✨"},
                "Mushroom Curry": {"price": "300", "description": "Mushroom curry, a creamy and flavorful dish made with fresh mushrooms simmered in a rich gravy. Perfect for mushroom lovers and pairs well with rice or naan. 🍄✨"},
                "Aloo Matar": {"price": "200", "description": "Aloo matar, a comforting dish made with potatoes and peas cooked in a mildly spiced gravy. A classic vegetarian option that is both filling and delicious. 🥔✨"},
                "Manchurian": {"price": "300", "description": "Manchurian, a popular Indo-Chinese dish made with your choice of vegetables or paneer, tossed in a tangy and spicy sauce. A perfect blend of flavors that is sure to satisfy. 🍜✨"},
                "Kalo Daal Jhaneko": {"price": "200", "description": "Kalo daal jhaneko, a traditional Nepali black lentil soup, rich in flavor and nutrients. Perfectly seasoned and served hot, ideal for a comforting meal. 🍲✨"}
            },
            "Non-Veg Main Course": {
                "Chicken Butter Masala": {"price": "500", "description": "Tender chicken pieces cooked in a rich and creamy butter masala sauce, infused with aromatic spices. A classic favorite that pairs perfectly with naan or rice. 🍗✨"},
                "Egg Curry": {"price": "300", "description": "Hard-boiled eggs simmered in a flavorful curry sauce, offering a delightful blend of spices. A comforting and satisfying dish for egg lovers. 🍳✨"},
                "Chicken Curry": {"price": "350", "description": "Juicy chicken pieces cooked in a traditional curry sauce, rich in spices and flavors. A hearty dish that brings warmth and comfort to your meal. 🍗✨"},
                "Manchurian (Chicken/Fish)": {"price": "450/550", "description": "A delicious Manchurian dish made with your choice of chicken or fish, tossed in a tangy and spicy sauce. Perfectly balanced flavors that are sure to satisfy your cravings. 🍗🐟✨"},
                "Fish Curry": {"price": "450", "description": "Fresh fish cooked in a tangy and spicy curry sauce, offering a delightful seafood experience. Perfectly seasoned and served hot. 🐟✨"},
                "Mutton Curry": {"price": "450", "description": "A rich and flavorful mutton curry, slow-cooked to perfection with a blend of spices. A hearty dish that is perfect for special occasions or a comforting meal. 🍖✨"},
                "Masaledar Mutton": {"price": "550", "description": "Masaledar mutton, a spicy and flavorful dish made with tender mutton pieces cooked in a rich and aromatic masala sauce. Perfect for those who love a bit of heat in their meal. 🍖🌶️✨"}
            },
            "Rice and Noodles": {
                "Rice (Plain, Jeera)": {"price": "125/150", "description": "Steamed rice served plain or with a hint of cumin (jeera). A perfect accompaniment to any main dish, light and fluffy. 🍚✨"},
                "Fried Rice (Veg, Egg, Chicken)": {"price": "200/225/250", "description": "Flavorful fried rice available in veg, chicken, or egg. Stir-fried with fresh vegetables and spices for a delightful meal. 🍚✨"},
                "Chowmein (Veg, Egg, Chicken)": {"price": "200/225/250", "description": "Savory chowmein noodles tossed with your choice of vegetables, chicken, or egg. A classic noodle dish that is both satisfying and delicious. 🍜✨"},
                "Thukpa (Plain, Veg, Chicken)": {"price": "200/225/250", "description": "Thukpa, a hearty noodle soup available in plain, veg, or chicken. Packed with flavors and perfect for a comforting meal. 🍜✨"},
                "Wai Wai Fry": {"price": "150", "description": "Wai Wai noodles stir-fried with vegetables and spices. A quick and tasty snack or meal option that is sure to satisfy your cravings. 🍜✨"}
            },
            "Roti and Breads": {
                "Plain Roti": {"price": "30", "description": "Soft and fluffy plain roti, perfect for scooping up your favorite curries. A staple in every Indian meal. 🍞✨"},
                "Butter Roti": {"price": "40", "description": "Delicious butter roti, brushed with melted butter for a rich and flavorful taste. A delightful addition to any meal. 🧈✨"},
                "Garlic Roti": {"price": "40", "description": "Flavorful garlic roti, infused with minced garlic and herbs. A perfect accompaniment to enhance the taste of your dishes. 🧄✨"},
                "Puri": {"price": "30", "description": "Crispy and fluffy puris, deep-fried to perfection. A popular choice for breakfast or as a side dish. 🥯✨"},
                "Lachha Paratha": {"price": "50", "description": "Lachha paratha, a layered flatbread that is crispy on the outside and soft on the inside. Perfect for enjoying with curries or gravies. 🥖✨"},
                "Naan (Plain, Butter, Garlic)": {"price": "50/60/70", "description": "Soft naan bread available in plain, butter, or garlic. A versatile bread that pairs well with a variety of dishes. 🍞✨"},
                "Tandoori Roti": {"price": "40", "description": "Tandoori roti, baked in a traditional tandoor oven for a smoky flavor. A healthy and delicious option to complement your meals. 🍞🔥✨"}
            },
            "Cold Beverages": {
                "Coca-Cola, Sprite, Fanta, Mountain Dew": {"price": "110", "description": "Refreshing and classic soft drinks to quench your thirst. Choose from Coca-Cola, Sprite, Fanta, or Mountain Dew for a fizzy delight. 🥤✨"},
                "Masala Coke": {"price": "80", "description": "A unique twist on the classic Coke, infused with a blend of spices for a refreshing and zesty flavor. Perfect for those who love a little extra kick! 🥤🌶️"},
                "Lemon Soda": {"price": "70", "description": "A refreshing blend of lemon and soda, served chilled. Perfect for a hot day, this drink is both tangy and thirst-quenching. 🍋✨"},
                "Mint Lemonade": {"price": "80", "description": "A refreshing mint lemonade, combining the zest of lemon with the coolness of mint. Perfect for a hot day, this drink is both tangy and refreshing. 🍋🌿✨"},
                "Mojito (Virgin, Strawberry, Mango)": {"price": "150/200/250", "description": "A refreshing mojito with a twist! Choose from classic virgin, fruity strawberry, or tropical mango flavors. Perfectly balanced with mint and lime for a refreshing sip. 🍹✨"},
                "Real Juice": {"price": "150", "description": "Pure and natural Real Juice, available in various flavors. A healthy and refreshing option to enjoy any time of the day. 🍊✨"},
                "Lassi (Sweet, Strawberry, Mango, Banana)": {"price": "120/150/180/200", "description": "Creamy and delicious lassi, available in sweet, strawberry, mango, or banana flavors. A perfect blend of yogurt and fruit for a refreshing drink. 🥛🍓🥭🍌✨"},
                "Milkshake (Banana, Strawberry, Mango, Chocolate)": {"price": "150/180/200/220", "description": "Thick and creamy milkshakes in banana, strawberry, mango, or chocolate flavors. A delightful treat for milkshake lovers! 🍌🍓🥭🍫✨"},
                "Cold Coffee": {"price": "120", "description": "Rich and creamy cold coffee, perfect for coffee lovers. A refreshing blend of coffee and milk, served chilled. ☕❄️✨"},
                "Mohi": {"price": "100", "description": "A traditional Nepali drink made with yogurt, water, and spices. Refreshing and nutritious, perfect for any time of the day. 🥛✨"},
                "Mineral Water": {"price": "60", "description": "Pure and refreshing mineral water, perfect for staying hydrated. A must-have with any meal or on a hot day. 💧✨"}
            },
            "Must Try": {
                "Crispy Momo (Chicken, Veg, Paneer)": {"price": "300/350/400", "description": "Crispy and flavorful momos, available in chicken, veg, or paneer. Perfectly steamed and served with a spicy dipping sauce. A must-try for momo lovers! 🥟✨"},
                "Jhaneko Momo (Chicken, Veg, Paneer)": {"price": "300/350/400", "description": "Jhaneko momos, a unique twist on the classic, available in chicken, veg, or paneer. Steamed to perfection and served with a tangy sauce. A delightful treat! 🥟✨"},
                "Mustang Momo (Chicken, Veg, Paneer)": {"price": "300/350/400", "description": "Mustang momos, a flavorful variation available in chicken, veg, or paneer. Steamed and served with a spicy sauce for an extra kick. A must-try for momo enthusiasts! 🥟✨"},
                "Hotwings": {"price": "400", "description": "Crispy and spicy hotwings, perfect for those who love a bit of heat. Served with a tangy dipping sauce for an extra kick. A must-try for wing lovers! 🍗🔥✨"},
                "Cheesy Ball": {"price": "250", "description": "Cheesy balls, crispy on the outside and gooey on the inside. A delightful snack for cheese lovers, served with a tangy dip. A must-try for a cheesy treat! 🧀✨"},
                "Chicken Finger": {"price": "300", "description": "Crispy chicken fingers, perfect for a quick snack or appetizer. Served with a tangy dipping sauce for an extra flavor boost. A must-try for chicken lovers! 🍗✨"},
                "Mix Pizza": {"price": "500", "description": "A delicious mix pizza topped with a variety of fresh ingredients. Perfectly baked with a crispy crust and a medley of flavors. A must-try for pizza enthusiasts! 🍕✨"},
                "Spicy Sausage Aloo": {"price": "350", "description": "Spicy sausage aloo, a flavorful dish with spicy sausages and potatoes. Perfectly seasoned and served hot. A must-try for those who love a bit of spice! 🌭✨"}
            },
            "Hot Beverages": {
                "Black Tea": {"price": "50", "description": "A classic black tea brewed to perfection, served hot and strong. Perfect for a refreshing start to your day or a cozy evening. ☕✨"},
                "Masala Tea": {"price": "60", "description": "A robust masala tea infused with a blend of spices, offering a warm and aromatic experience. Perfect for those who love a spicy kick in their tea. ☕🌶️✨"},
                "Ginger Tea": {"price": "60", "description": "A soothing ginger tea made with fresh ginger, providing a warm and comforting drink. Ideal for cold days or when you're feeling under the weather. ☕🌿✨"},
                "Lemon Tea": {"price": "60", "description": "A refreshing lemon tea with a zesty twist, combining the warmth of tea with the tanginess of lemon. Perfect for a refreshing pick-me-up. ☕🍋✨"},
                "Coffee (Black, White)": {"price": "70/80", "description": "A rich and aromatic coffee, available in black for a strong flavor or white for a creamy touch. Perfect for coffee lovers looking for a caffeine boost. ☕✨"},
                "Milk Tea": {"price": "70", "description": "A creamy milk tea made with fresh milk and brewed tea, offering a comforting and rich flavor. Perfect for a cozy afternoon break. ☕🥛✨"},
                "Green Tea": {"price": "70", "description": "A refreshing green tea, known for its health benefits and light flavor. Perfect for a calming and rejuvenating drink. 🍵✨"},
                "Matka Tandoori Tea": {"price": "100", "description": "A unique matka tandoori tea served in a traditional clay pot, offering a smoky flavor and a rustic experience. Perfect for those who enjoy a traditional touch. ☕🔥✨"}
            }
        }
    
    def clear_scrollable_frame(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        self.clear_scrollable_frame()
        
        title_label = tk.Label(self.scrollable_frame, text="Main Menu", font=("Arial", 20, "bold"), 
                              bg="#f5f5f5", fg="#d32f2f")
        title_label.pack(pady=20)
        
        categories = list(self.menu_data.keys())
        categories.sort()
        
        for category in categories:
            btn = tk.Button(self.scrollable_frame, text=category, font=("Arial", 14), 
                           bg="#d32f2f", fg="white", width=30, height=2,
                           command=lambda c=category: self.show_category_items(c))
            btn.pack(pady=10)
    
    def show_category_items(self, category):
        self.clear_scrollable_frame()
        
        title_label = tk.Label(self.scrollable_frame, text=category, font=("Arial", 20, "bold"), 
                              bg="#f5f5f5", fg="#d32f2f")
        title_label.pack(pady=20)
        
        items_frame = tk.Frame(self.scrollable_frame, bg="#f5f5f5")
        items_frame.pack(fill="both", expand=True, padx=20)
        
        row = 0
        col = 0
        for item_name, item_data in self.menu_data[category].items():
            item_frame = tk.Frame(items_frame, bg="white", relief="raised", bd=2)
            item_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            name_label = tk.Label(item_frame, text=item_name, font=("Arial", 12, "bold"), 
                                 bg="white", wraplength=250, justify="center")
            name_label.pack(pady=10, padx=10)
            
            price_label = tk.Label(item_frame, text=f"Rs. {item_data['price']}", 
                                  font=("Arial", 11, "bold"), bg="white", fg="#d32f2f")
            price_label.pack(pady=5)
            
            short_desc = item_data['description'][:80] + "..." if len(item_data['description']) > 80 else item_data['description']
            desc_label = tk.Label(item_frame, text=short_desc, font=("Arial", 9), 
                                 bg="white", wraplength=250, justify="center")
            desc_label.pack(pady=5, padx=10)
            
            details_btn = tk.Button(item_frame, text="View Details", font=("Arial", 10),
                                   bg="#4caf50", fg="white",
                                   command=lambda n=item_name, c=category: self.show_item_details(n, c))
            details_btn.pack(pady=10)
            
            col += 1
            if col > 2:  
                col = 0
                row += 1
        
        for i in range(3):
            items_frame.grid_columnconfigure(i, weight=1)
    
    def show_item_details(self, item_name, category):
        self.clear_scrollable_frame()
        
        item_data = self.menu_data[category][item_name]
        
        back_btn = tk.Button(self.scrollable_frame, text="← Back to Menu", font=("Arial", 10),
                            bg="#757575", fg="white", command=lambda: self.show_category_items(category))
        back_btn.pack(anchor="w", padx=20, pady=10)
        
        details_frame = tk.Frame(self.scrollable_frame, bg="white", relief="raised", bd=2)
        details_frame.pack(fill="both", expand=True, padx=50, pady=20)
        
        name_label = tk.Label(details_frame, text=item_name, font=("Arial", 18, "bold"), 
                             bg="white", fg="#d32f2f")
        name_label.pack(pady=20)
        
        price_label = tk.Label(details_frame, text=f"Price: Rs. {item_data['price']}", 
                              font=("Arial", 14, "bold"), bg="white")
        price_label.pack(pady=10)
    
        desc_label = tk.Label(details_frame, text=item_data['description'], font=("Arial", 12), 
                             bg="white", wraplength=600, justify="center")
        desc_label.pack(pady=20, padx=30)
        
def main():
    root = tk.Tk()
    app = DaloRestaurantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()