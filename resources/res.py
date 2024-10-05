print("""test_cases = {
    "TEST-1": {
        "description": "Display configurable products",
        "requirements": "Functionality - Product Configuration - Display configurable products",
        "steps": [
            "Navigate to the product configuration page.",
            "Verify that a list of configurable products is displayed."
        ],
        "expected_result": "A list of configurable products is displayed."
    },
    "TEST-2": {
        "description": "Select product for configuration",
        "requirements": "Functionality - Product Configuration - Allow product selection for configuration",
        "steps": [
            "Navigate to the product configuration page.",
            "Select a product from the list of configurable products.",
            "Verify that the selected product is displayed for configuration."
        ],
        "expected_result": "The selected product is displayed for configuration."
    },
    "TEST-3": {
        "description": "Display available components for configuration",
        "requirements": "Functionality - Product Configuration - Display available components for configuration",
        "steps": [
            "Navigate to the product configuration page.",
            "Select a product for configuration.",
            "Verify that a list of available components for the selected product is displayed."
        ],
        "expected_result": "A list of available components for the selected product is displayed."
    },
    "TEST-4": {
        "description": "Add component to configuration",
        "requirements": "Functionality - Product Configuration - Enable adding components to configuration",
        "steps": [
            "Navigate to the product configuration page.",
            "Select a product for configuration.",
            "Select a component from the list of available components.",
            "Click on the 'Add' button.",
            "Verify that the selected component is added to the product configuration."
        ],
        "expected_result": "The selected component is added to the product configuration."
    },
    "TEST-5": {
        "description": "Notify about configuration conflicts",
        "requirements": "Functionality - Product Configuration - Notify about configuration conflicts",
        "steps": [
            "Navigate to the product configuration page.",
            "Select a product for configuration.",
            "Add components to the configuration that result in a conflict.",
            "Verify that a notification about the configuration conflict is displayed."
        ],
        "expected_result": "A notification about the configuration conflict is displayed."
    },
    "TEST-6": {
        "description": "Update configuration to resolve conflicts",
        "requirements": "Functionality - Product Configuration - Allow configuration update to resolve conflicts",
        "steps": [
            "Navigate to the product configuration page.",
            "Select a product for configuration.",
            "Add components to the configuration that result in a conflict.",
            "Update the configuration to resolve the conflict.",
            "Verify that the configuration is updated and the conflict is resolved."
        ],
        "expected_result": "The configuration is updated and the conflict is resolved."
    },
    "TEST-7": {
        "description": "Confirm configuration completion",
        "requirements": "Functionality - Product Configuration - Allow configuration completion confirmation",
        "steps": [
            "Navigate to the product configuration page.",
            "Select a product for configuration.",
            "Add components to the configuration.",
            "Click on the 'Confirm' button.",
            "Verify that a confirmation message is displayed, confirming the completion of the configuration."
        ],
        "expected_result": "A confirmation message is displayed, confirming the completion of the configuration."
    },
    "TEST-8": {
        "description": "Display detailed product information",
        "requirements": "Functionality - Product Details - Display detailed information of selected products",
        "steps": [
            "Navigate to the product details page.",
            "Select a product.",
            "Verify that the detailed information of the selected product is displayed."
        ],
        "expected_result": "The detailed information of the selected product is displayed."
    },
    "TEST-9": {
        "description": "Provide browsing options for product details",
        "requirements": "Functionality - Product Details - Provide browsing options for product details",
        "steps": [
            "Navigate to the product details page.",
            "Verify that browsing options such as 'next,' 'previous,' 'related products,' etc., are available."
        ],
        "expected_result": "Browsing options such as 'next,' 'previous,' 'related products,' etc., are available."
    },
    "TEST-10": {
        "description": "Display detailed product categorization",
        "requirements": "Functionality - Product Categorization - Display detailed product categorization",
        "steps": [
            "Navigate to the product category page.",
            "Verify that a detailed product categorization is displayed."
        ],
        "expected_result": "A detailed product categorization is displayed."
    },
    "TEST-11": {
        "description": "Enable search text input",
        "requirements": "Functionality - Search - Enable search text input",
        "steps": [
            "Navigate to the search page.",
            "Verify that a search text input field is available."
        ],
        "expected_result": "A search text input field is available."
    },
    "TEST-12": {
        "description": "Enable multiple search option selections",
        "requirements": "Functionality - Search - Enable multiple search option selections",
        "steps": [
            "Navigate to the search page.",
            "Verify that multiple search options, such as category, price range, etc., can be selected."
        ],
        "expected_result": "Multiple search options, such as category, price range, etc., can be selected."
    },
    "TEST-13": {
        "description": "Display matching products based on search",
        "requirements": "Functionality - Search - Display matching products based on search",
        "steps": [
            "Navigate to the search page.",
            "Enter search criteria.",
            "Verify that matching products based on the search criteria are displayed."
        ],
        "expected_result": "Matching products based on the search criteria are displayed."
    },
    "TEST-14": {
        "description": "Display 10 matching results per screen",
        "requirements": "Functionality - Search - Display 10 matching results per screen",
        "steps": [
            "Navigate to the search page.",
            "Enter search criteria that yield more than 10 matching products.",
            "Verify that only 10 matching results are displayed per screen."
        ],
        "expected_result": "Only 10 matching results are displayed per screen."
    },
    "TEST-15": {
        "description": "Enable navigation between search results",
        "requirements": "Functionality - Search - Enable navigation between search results",
        "steps": [
            "Navigate to the search page.",
            "Enter search criteria that yield more than 10 matching products.",
            "Verify that navigation options, such as pagination or 'next' and 'previous' buttons, are available to browse through all search results."
        ],
        "expected_result": "Navigation options, such as pagination or 'next' and 'previous' buttons, are available to browse through all search results."
    },
    "TEST-16": {
        "description": "Notify when no matching product is found",
        "requirements": "Functionality - Search - Notify when no matching product is found",
        "steps": [
            "Navigate to the search page.",
            "Enter search criteria that do not match any product.",
            "Verify that a notification message is displayed, indicating that no matching product was found."
        ],
        "expected_result": "A notification message is displayed, indicating that no matching product was found."
    },
    "TEST-17": {
        "description": "Allow profile creation and credential setting",
        "requirements": "Functionality - Customer Profile - Allow profile creation and credential setting",
        "steps": [
            "Navigate to the customer profile creation page.",
            "Enter the required information for profile creation.",
            "Set the credentials for the profile.",
            "Verify that the profile is created successfully with the set credentials."
        ],
        "expected_result": "The profile is created successfully with the set credentials."
    },
    "TEST-18": {
        "description": "Authenticate credentials for profile view",
        "requirements": "Functionality - Customer Profile - Authenticate credentials for profile view",
        "steps": [
            "Navigate to the customer profile login page.",
            "Enter the correct credentials for an existing profile.",
            "Verify that the user is authenticated and redirected to the profile view page."
        ],
        "expected_result": "The user is authenticated and redirected to the profile view page."
    },
    "TEST-19": {
        "description": "Allow profile information update",
        "requirements": "Functionality - Customer Profile - Allow profile information update",
        "steps": [
            "Navigate to the customer profile edit page.",
            "Update the profile information.",
            "Save the changes.",
            "Verify that the profile information is updated successfully."
        ],
        "expected_result": "The profile information is updated successfully."
    },
    "TEST-20": {
        "description": "Display active and completed order history",
        "requirements": "Functionality - Customer Profile - Display active and completed order history",
        "steps": [
            "Navigate to the customer profile order history page.",
            "Verify that both active and completed orders are displayed in the order history."
        ],
        "expected_result": "Both active and completed orders are displayed in the order history."
    },
    "TEST-21": {
        "description": "Allow order selection from history",
        "requirements": "Functionality - Customer Profile - Allow order selection from history",
        "steps": [
            "Navigate to the customer profile order history page.",
            "Select an order from the order history.",
            "Verify that the details of the selected order are displayed."
        ],
        "expected_result": "The details of the selected order are displayed."
    },
    "TEST-22": {
        "description": "Display detailed information about the selected order",
        "requirements": "Functionality - Customer Profile - Display detailed information about selected order",
        "steps": [
            "Navigate to the customer profile order history page.",
            "Select an order from the order history.",
            "Verify that detailed information about the selected order, such as order date, items ordered, shipping address, billing information, etc., is displayed."
        ],
        "expected_result": "Detailed information about the selected order, such as order date, items ordered, shipping address, billing information, etc., is displayed."
    },
    "TEST-23": {
        "description": "Display frequently searched items",
        "requirements": "Functionality - Customer Profile - Display frequently searched items",
        "steps": [
            "Navigate to the customer profile page.",
            "Verify that a section displaying frequently searched items is present."
        ],
        "expected_result": "A section displaying frequently searched items is present."
    },
    "TEST-24": {
        "description": "Allow newsletter and survey registration",
        "requirements": "Functionality - Customer Profile - Allow newsletter and survey registration",
        "steps": [
            "Navigate to the customer profile page.",
            "Verify that options for newsletter and survey registration are available."
        ],
        "expected_result": "Options for newsletter and survey registration are available."
    },
    "TEST-25": {
        "description": "Provide online help, FAQs, customer support, and sitemap options",
        "requirements": "Functionality - Customer Support - Provide online help, FAQs, customer support, and sitemap options",
        "steps": [
            "Navigate to the customer support page.",
            "Verify that options for online help, FAQs, customer support, and sitemap are available."
        ],
        "expected_result": "Options for online help, FAQs, customer support, and sitemap are available."
    },
    "TEST-26": {
        "description": "Allow support type selection",
        "requirements": "Functionality - Customer Support - Allow support type selection",
        "steps": [
            "Navigate to the customer support page.",
            "Verify that users can select different support types, such as technical support, billing support, etc."
        ],
        "expected_result": "Users can select different support types, such as technical support, billing support, etc."
    },
    "TEST-27": {
        "description": "Allow input of customer and product information for support",
        "requirements": "Functionality - Customer Support - Allow input of customer and product information for support",
        "steps": [
            "Navigate to the customer support page.",
            "Verify that fields are available for users to input customer information and product information."
        ],
        "expected_result": "Fields are available for users to input customer information and product information."
    },
    "TEST-28": {
        "description": "Display customer support contact numbers",
        "requirements": "Functionality - Customer Support - Display customer support contact numbers",
        "steps": [
            "Navigate to the customer support page.",
            "Verify that customer support contact numbers are displayed."
        ],
        "expected_result": "Customer support contact numbers are displayed."
    },
    "TEST-29": {
        "description": "Allow contact number input for support calls",
        "requirements": "Functionality - Customer Support - Allow contact number input for support calls",
        "steps": [
            "Navigate to the customer support page.",
            "Verify that a field is available for users to enter their contact number for support calls."
        ],
        "expected_result": "A field is available for users to enter their contact number for support calls."
    },
    "TEST-30": {
        "description": "Display online help upon request",
        "requirements": "Functionality - Customer Support - Display online help upon request",
        "steps": [
            "Navigate to the customer support page.",
            "Click on the 'Online Help' option.",
            "Verify that the online help content is displayed."
        ],
        "expected_result": "The online help content is displayed."
    },
    "TEST-31": {
        "description": "Display FAQs upon request",
        "requirements": "Functionality - Customer Support - Display FAQs upon request",
        "steps": [
            "Navigate to the customer support page.",
            "Click on the 'FAQs' option.",
            "Verify that the FAQs content is displayed."
        ],
        "expected_result": "The FAQs content is displayed."
    },
    "TEST-32": {
        "description": "Maintain customer email information as required",
        "requirements": "Functionality - Email Confirmation - Maintain customer email information as required",
        "steps": [
            "Verify that the system has a mechanism to store and retrieve customer email information.",
            "Verify that the system complies with privacy regulations regarding the storage and use of customer email information."
        ],
        "expected_result": "The system has a mechanism to store and retrieve customer email information while complying with privacy regulations."
    },
    "TEST-33": {
        "description": "Send order confirmation email",
        "requirements": "Functionality - Email Confirmation - Send order confirmation email",
        "steps": [
            "Place an order.",
            "Verify that an order confirmation email is sent to the customer's email address."
        ],
        "expected_result": "An order confirmation email is sent to the customer's email address."
    },
    "TEST-34": {
        "description": "Display detailed invoice for confirmed orders",
        "requirements": "Functionality - Invoice - Display detailed invoice for confirmed orders",
        "steps": [
            "Place an order and confirm it.",
            "Navigate to the order details page.",
            "Verify that a detailed invoice for the confirmed order is displayed."
        ],
        "expected_result": "A detailed invoice for the confirmed order is displayed."
    },
    "TEST-35": {
        "description": "Optionally allow invoice printing",
        "requirements": "Functionality - Invoice - Optionally allow invoice printing",
        "steps": [
            "Place an order and confirm it.",
            "Navigate to the order details page.",
            "Verify that an option to print the invoice is available."
        ],
        "expected_result": "An option to print the invoice is available."
    },
    "TEST-36": {
        "description": "Provide shopping cart during purchase",
        "requirements": "Functionality - Shopping Cart - Provide shopping cart during purchase",
        "steps": [
            "Add products to the cart.",
            "Verify that the shopping cart is accessible and displays the added products."
        ],
        "expected_result": "The shopping cart is accessible and displays the added products."
    },
    "TEST-37": {
        "description": "Allow adding/removing products in the cart",
        "requirements": "Functionality - Shopping Cart - Allow adding/removing products in the cart",
        "steps": [
            "Add products to the cart.",
            "Verify that options to add or remove products from the cart are available and functional."
        ],
        "expected_result": "Options to add or remove products from the cart are available and functional."
    },
    "TEST-38": {
        "description": "Display shipping options",
        "requirements": "Functionality - Shipping - Display shipping options",
        "steps": [
            "Proceed to the shipping page during checkout.",
            "Verify that available shipping options are displayed."
        ],
        "expected_result": "Available shipping options are displayed."
    },
    "TEST-39": {
        "description": "Enable shipping method selection during payment",
        "requirements": "Functionality - Shipping - Enable shipping method selection during payment",
        "steps": [
            "Proceed to the payment page during checkout.",
            "Verify that the option to select a shipping method is available."
        ],
        "expected_result": "The option to select a shipping method is available."
    },
    "TEST-40": {
        "description": "Display shipping charges",
        "requirements": "Functionality - Shipping - Display shipping charges",
        "steps": [
            "Proceed to the shipping page during checkout.",
            "Select a shipping method.",
            "Verify that the shipping charges for the selected method are displayed."
        ],
        "expected_result": "The shipping charges for the selected method are displayed."
    },
    "TEST-41": {
        "description": "Display estimated shipping duration",
        "requirements": "Functionality - Shipping - Display estimated shipping duration",
        "steps": [
            "Proceed to the shipping page during checkout.",
            "Select a shipping method.",
            "Verify that the estimated shipping duration for the selected method is displayed."
        ],
        "expected_result": "The estimated shipping duration for the selected method is displayed."
    },
    "TEST-42": {
        "description": "Allow order tracking with order information input",
        "requirements": "Functionality - Shipping - Allow order tracking with order information input",
        "steps": [
            "Navigate to the order tracking page.",
            "Enter the order information.",
            "Verify that the order tracking information is displayed."
        ],
        "expected_result": "The order tracking information is displayed."
    },
    "TEST-43": {
        "description": "Display current order tracking information",
        "requirements": "Functionality - Shipping - Display current order tracking information",
        "steps": [
            "Navigate to the order tracking page.",
            "Enter the order information.",
            "Verify that the current order tracking information, such as shipping status, estimated delivery date, etc., is displayed."
        ],
        "expected_result": "The current order tracking information, such as shipping status, estimated delivery date, etc., is displayed."
    },
    "TEST-44": {
        "description": "Calculate order tax",
        "requirements": "Functionality - Tax Calculation - Calculate order tax",
        "steps": [
            "Add products to the cart.",
            "Proceed to the payment page during checkout.",
            "Verify that the order tax is calculated and displayed."
        ],
        "expected_result": "The order tax is calculated and displayed."
    },
    "TEST-45": {
        "description": "Display tax information for the order",
        "requirements": "Functionality - Tax Calculation - Display tax information for the order",
        "steps": [
            "Add products to the cart.",
            "Proceed to the payment page during checkout.",
            "Verify that the tax information, such as tax rate and total tax amount, is displayed."
        ],
        "expected_result": "The tax information, such as tax rate and total tax amount, is displayed."
    },
    "TEST-46": {
        "description": "Display available payment methods",
        "requirements": "Functionality - Payment - Display available payment methods",
        "steps": [
            "Proceed to the payment page during checkout.",
            "Verify that the available payment methods are displayed."
        ],
        "expected_result": "The available payment methods are displayed."
    },
    "TEST-47": {
        "description": "Allow payment method selection",
        "requirements": "Functionality - Payment - Allow payment method selection",
        "steps": [
            "Proceed to the payment page during checkout.",
            "Verify that an option to select a payment method is available."
        ],
        "expected_result": "An option to select a payment method is available."
    },
    "TEST-48": {
        "description": "Display orders eligible for change",
        "requirements": "Functionality - Order Modification - Display orders eligible for change",
        "steps": [
            "Navigate to the order modification page.",
            "Verify that only orders eligible for change are displayed."
        ],
        "expected_result": "Only orders eligible for change are displayed."
    },
    "TEST-49": {
        "description": "Allow order selection for change",
        "requirements": "Functionality - Order Modification - Allow order selection for change",
        "steps": [
            "Navigate to the order modification page.",
            "Verify that an option to select an order for change is available."
        ],
        "expected_result": "An option to select an order for change is available."
    },
    "TEST-50": {
        "description": "Allow order cancellation",
        "requirements": "Functionality - Order Modification - Allow order cancellation",
        "steps": [
            "Navigate to the order modification page.",
            "Select an order.",
            "Verify that an option to cancel the order is available."
        ],
        "expected_result": "An option to cancel the order is available."
    },
    "TEST-51": {
        "description": "Allow changing shipping and payment methods",
        "requirements": "Functionality - Order Modification - Allow changing shipping and payment methods",
        "steps": [
            "Navigate to the order modification page.",
            "Select an order.",
            "Verify that options to change the shipping and payment methods are available."
        ],
        "expected_result": "Options to change the shipping and payment methods are available."
    },
    "TEST-52": {
        "description": "Notify about order changes",
        "requirements": "Functionality - Order Modification - Notify about order changes",
        "steps": [
            "Make changes to an order.",
            "Verify that a notification about the order changes is sent to the customer."
        ],
        "expected_result": "A notification about the order changes is sent to the customer."
    },
    "TEST-53": {
        "description": "Display product reviews and ratings",
        "requirements": "Functionality - Product Reviews - Display product reviews and ratings",
        "steps": [
            "Navigate to the product details page.",
            "Verify that product reviews and ratings are displayed."
        ],
        "expected_result": "Product reviews and ratings are displayed."
    },
    "TEST-54": {
        "description": "Enable users to enter reviews and ratings",
        "requirements": "Functionality - Product Reviews - Enable users to enter reviews and ratings",
        "steps": [
            "Navigate to the product details page.",
            "Verify that options for users to enter reviews and ratings are available."
        ],
        "expected_result": "Options for users to enter reviews and ratings are available."
    },
    "TEST-55": {
        "description": "Display available financing options",
        "requirements": "Functionality - Financing - Display available financing options",
        "steps": [
            "Proceed to the payment page during checkout.",
            "Verify that available financing options are displayed."
        ],
        "expected_result": "Available financing options are displayed."
    },
    "TEST-56": {
        "description": "Allow financing option selection",
        "requirements": "Functionality - Financing - Allow financing option selection",
        "steps": [
            "Proceed to the payment page during checkout.",
            "Verify that an option to select a financing option is available."
        ],
        "expected_result": "An option to select a financing option is available."
    },
    "TEST-57": {
        "description": "Notify about financing requests",
        "requirements": "Functionality - Financing - Notify about financing requests",
        "steps": [
            "Submit a financing request.",
            "Verify that a notification about the financing request is sent to the relevant parties."
        ],
        "expected_result": "A notification about the financing request is sent to the relevant parties."
    },
    "TEST-58": {
        "description": "Provide a detailed sitemap",
        "requirements": "Functionality - Sitemap - Provide a detailed sitemap",
        "steps": [
            "Navigate to the sitemap page.",
            "Verify that a detailed sitemap of the website is displayed."
        ],
        "expected_result": "A detailed sitemap of the website is displayed."
    },
    "TEST-59": {
        "description": "Display available promotions",
        "requirements": "Functionality - Promotions - Display available promotions",
        "steps": [
            "Navigate to the promotions page.",
            "Verify that available promotions are displayed."
        ],
        "expected_result": "Available promotions are displayed."
    },
    "TEST-60": {
        "description": "Allow promotion selection",
        "requirements": "Functionality - Promotions - Allow promotion selection",
        "steps": [
            "Navigate to the promotions page.",
            "Verify that an option to select a promotion is available."
        ],
        "expected_result": "An option to select a promotion is available."
    },
    "TEST-61": {
        "description": "Allow purchase confirmation",
        "requirements": "Functionality - Purchase - Allow purchase confirmation",
        "steps": [
            "Proceed to the payment page during checkout.",
            "Verify that an option to confirm the purchase is available."
        ],
        "expected_result": "An option to confirm the purchase is available."
    },
    "TEST-62": {
        "description": "Enable payment information input",
        "requirements": "Functionality - Purchase - Enable payment information input",
        "steps": [
            "Proceed to the payment page during checkout.",
            "Verify that fields are available for users to enter payment information."
        ],
        "expected_result": "Fields are available for users to enter payment information."
    },
    "TEST-63": {
        "description": "Uniform look and feel across web pages",
        "requirements": "Usability - GUI - Uniform look and feel across web pages",
        "steps": [
            "Navigate through different web pages of the website.",
            "Verify that a consistent look and feel is maintained across all pages."
        ],
        "expected_result": "A consistent look and feel is maintained across all pages."
    },
    "TEST-64": {
        "description": "Digital image for each product in the catalog",
        "requirements": "Usability - GUI - Digital image for each product in the catalog",
        "steps": [
            "Navigate to the product catalog.",
            "Verify that each product in the catalog has a digital image."
        ],
        "expected_result": "Each product in the catalog has a digital image."
    },
    "TEST-65": {
        "description": "Use of icons and toolbars",
        "requirements": "Usability - GUI - Use of icons and toolbars",
        "steps": [
            "Navigate through different web pages of the website.",
            "Verify that icons and toolbars are used appropriately to enhance user experience."
        ],
        "expected_result": "Icons and toolbars are used appropriately to enhance user experience."
    },
    "TEST-66": {
        "description": "Handicap access",
        "requirements": "Usability - Accessibility - Handicap access",
        "steps": [
            "Verify that the website is designed to be accessible to users with disabilities.",
            "Test the website using accessibility testing tools."
        ],
        "expected_result": "The website is accessible to users with disabilities, as validated by accessibility testing tools."
    },
    "TEST-67": {
        "description": "Multi-language support",
        "requirements": "Usability - Accessibility - Multi-language support",
        "steps": [
            "Verify that the website supports multiple languages.",
            "Test the language switching functionality."
        ],
        "expected_result": "The website supports multiple languages, and the language switching functionality works as expected."
    },
    "TEST-68": {
        "description": "Redundant computer storage for databases with automatic switchover",
        "requirements": "Reliability & Availability - Backend - Redundant computer storage for databases with automatic switchover",
        "steps": [
            "Simulate a failure of the primary database server.",
            "Verify that the system automatically switches over to the redundant database server without data loss or downtime."
        ],
        "expected_result": "The system automatically switches over to the redundant database server without data loss or downtime."
    },
    "TEST-69": {
        "description": "Database replication to off-site locations",
        "requirements": "Reliability & Availability - Backend - Database replication to off-site locations",
        "steps": [
            "Verify that the database is replicated to off-site locations for disaster recovery purposes."
        ],
        "expected_result": "The database is replicated to off-site locations for disaster recovery purposes."
    },
    "TEST-70": {
        "description": "RAID V Disk Stripping on database storage disks",
        "requirements": "Reliability & Availability - Backend - RAID V Disk Stripping on database storage disks",
        "steps": [
            "Verify that RAID V Disk Stripping is implemented on the database storage disks for data protection and redundancy."
        ],
        "expected_result": "RAID V Disk Stripping is implemented on the database storage disks."
    },
    "TEST-71": {
        "description": "Contractual agreement with ISP for T3 access with 99.9999% availability",
        "requirements": "Reliability & Availability - Internet Service Provider - Contractual agreement with ISP for T3 access with 99.9999% availability",
        "steps": [
            "Review the contractual agreement with the ISP.",
            "Verify that the agreement includes provisions for T3 access with 99.9999% availability."
        ],
        "expected_result": "The contractual agreement includes provisions for T3 access with 99.9999% availability."
    },
    "TEST-72": {
        "description": "Contractual agreement with ISP for 99.999% network availability",
        "requirements": "Reliability & Availability - Internet Service Provider - Contractual agreement with ISP for 99.999% network availability",
        "steps": [
            "Review the contractual agreement with the ISP.",
            "Verify that the agreement includes provisions for 99.999% network availability."
        ],
        "expected_result": "The contractual agreement includes provisions for 99.999% network availability."
    },
    "TEST-73": {
        "description": "Web-based product running on a web server",
        "requirements": "Performance - Web-based product running on a web server",
        "steps": [
            "Verify that the product is accessible through a web browser.",
            "Verify that the product is hosted on a web server."
        ],
        "expected_result": "The product is accessible through a web browser and hosted on a web server."
    },
    "TEST-74": {
        "description": "Initial load time dependent on internet connection strength",
        "requirements": "Performance - Initial load time dependent on internet connection strength",
        "steps": [
            "Test the initial load time of the website using different internet connection speeds.",
            "Verify that the initial load time varies depending on the internet connection strength."
        ],
        "expected_result": "The initial load time varies depending on the internet connection strength."
    },
    "TEST-75": {
        "description": "Performance dependent on client hardware",
        "requirements": "Performance - Performance dependent on client hardware",
        "steps": [
            "Test the performance of the website using different client hardware configurations.",
            "Verify that the performance varies depending on the client hardware."
        ],
        "expected_result": "The performance varies depending on the client hardware."
    },
    "TEST-76": {
        "description": "Use secure sockets for transactions with confidential information",
        "requirements": "Security - Data Transfer - Use secure sockets for transactions with confidential information",
        "steps": [
            "Initiate a transaction that involves confidential information.",
            "Verify that the transaction is performed over a secure socket layer (SSL).",
            "Verify that the website uses HTTPS for secure communication."
        ],
        "expected_result": "The transaction is performed over SSL, and the website uses HTTPS."
    },
    "TEST-77": {
        "description": "Automatic customer logout after inactivity",
        "requirements": "Security - Data Transfer - Automatic customer logout after inactivity",
        "steps": [
            "Log in to the website.",
            "Remain inactive for a predefined period.",
            "Verify that the system automatically logs out the user after the inactivity period."
        ],
        "expected_result": "The system automatically logs out the user after the inactivity period."
    },
    "TEST-78": {
        "description": "Transaction confirmation with customer's web browser",
        "requirements": "Security - Data Transfer - Transaction confirmation with customer's web browser",
        "steps": [
            "Complete a transaction.",
            "Verify that a transaction confirmation message is displayed in the customer's web browser."
        ],
        "expected_result": "A transaction confirmation message is displayed in the customer's web browser."
    },
    "TEST-79": {
        "description": "No cookies containing user passwords",
        "requirements": "Security - Data Transfer - No cookies containing user passwords",
        "steps": [
            "Log in to the website.",
            "Examine the cookies stored by the website.",
            "Verify that no cookies contain user passwords."
        ],
        "expected_result": "No cookies contain user passwords."
    },
    "TEST-80": {
        "description": "No cookies containing confidential information",
        "requirements": "Security - Data Transfer - No cookies containing confidential information",
        "steps": [
            "Perform actions that involve confidential information.",
            "Examine the cookies stored by the website.",
            "Verify that no cookies contain confidential information."
        ],
        "expected_result": "No cookies contain confidential information."
    },""")