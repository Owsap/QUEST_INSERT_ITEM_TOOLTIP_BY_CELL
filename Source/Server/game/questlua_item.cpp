/// 1.
// Search
	int item_get_cell(lua_State* L)

// Add above
	int item_get_window_type(lua_State* L)
	{
		CQuestManager& q = CQuestManager::instance();
		if (q.GetCurrentItem())
			lua_pushnumber(L, q.GetCurrentItem()->GetWindow());
		else
			lua_pushnumber(L, RESERVED_WINDOW);
		return 1;
	}

/// 2.
// Search
			{ "get_cell", item_get_cell },

// Add above
			{ "get_window_type", item_get_window_type },