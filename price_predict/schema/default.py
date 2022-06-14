class ModelConstant:
    __furniture  = {
        "barang": {}
    }

    @staticmethod
    def processing(height, depth, width, cost, category, materials):
        ModelConstant.__furniture["barang"]["height"] = height 
        ModelConstant.__furniture["barang"]["depth"] = depth 
        ModelConstant.__furniture["barang"]["width"] = width
        ModelConstant.__furniture["barang"]["cost"] = cost

        if category == "Beds":
            ModelConstant.__furniture["barang"]["Beds"] = 1.0
            ModelConstant.__furniture["barang"]["Chairs"] = 0.0
            ModelConstant.__furniture["barang"]["Tables & Desks"] = 0.0
            ModelConstant.__furniture["barang"]["Wardrobes"] = 0.0
        elif category == "Chairs":
            ModelConstant.__furniture["barang"]["Beds"] = 0.0
            ModelConstant.__furniture["barang"]["Chairs"] = 1.0
            ModelConstant.__furniture["barang"]["Tables & Desks"] = 0.0
            ModelConstant.__furniture["barang"]["Wardrobes"] = 0.0
        elif category == "Tables & Desks":
            ModelConstant.__furniture["barang"]["Beds"] = 0.0
            ModelConstant.__furniture["barang"]["Chairs"] = 0.0
            ModelConstant.__furniture["barang"]["Tables & Desks"] = 1.0
            ModelConstant.__furniture["barang"]["Wardrobes"] = 0.0
        elif category == "Wardrobes":
            ModelConstant.__furniture["barang"]["Beds"] = 0.0
            ModelConstant.__furniture["barang"]["Chairs"] = 0.0
            ModelConstant.__furniture["barang"]["Tables & Desks"] = 0.0
            ModelConstant.__furniture["barang"]["Wardrobes"] = 1.0
        
        if materials == "Plastic":
            ModelConstant.__furniture["barang"]["Plastic"] = 1.0
            ModelConstant.__furniture["barang"]["Steel"] = 0.0
            ModelConstant.__furniture["barang"]["Wood"] = 0.0
        elif materials == "Steel":
            ModelConstant.__furniture["barang"]["Plastic"] = 0.0
            ModelConstant.__furniture["barang"]["Steel"] = 1.0
            ModelConstant.__furniture["barang"]["Wood"] = 0.0
        elif materials == "Wood":
            ModelConstant.__furniture["barang"]["Plastic"] = 0.0
            ModelConstant.__furniture["barang"]["Steel"] = 0.0
            ModelConstant.__furniture["barang"]["Wood"] = 1.0
        
        return ModelConstant.__furniture["barang"]