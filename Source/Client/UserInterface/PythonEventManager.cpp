/// 1.
// Search
	case EVENT_TYPE_SELECT_ITEM:
	{
		PyCallClassMemberFunc(m_poInterface, "BINARY_OpenSelectItemWindow", Py_BuildValue("()"));
		break;
	}

// Add below
	case EVENT_TYPE_INSERT_ITEM_TOOLTIP_BY_CELL:
	{
		int iWindowType = atoi(GetArgument("window_type", ScriptCommand.argList));
		int iCell= atoi(GetArgument("cell", ScriptCommand.argList));

		PyCallClassMemberFunc(pEventSet->poEventHandler, "OnInsertImageShowItemToolTipByCell", Py_BuildValue("(ii)", iWindowType, iCell));

		CPythonPlayer& rkPlayer = CPythonPlayer::Instance();
		DWORD dwItemIndex = rkPlayer.GetItemIndex(TItemPos(iWindowType, iCell));

		CItemManager::Instance().SelectItemData(dwItemIndex);
		CItemData* pItemData = CItemManager::Instance().GetSelectedItemDataPointer();
		int iAdjustLine = 2;
		if (pItemData)
			iAdjustLine = iAdjustLine * pItemData->GetSize();

		pEventSet->iAdjustLine += iAdjustLine;
		break;
	}

/// 2.
// Search
	EventTypeMap["SELECT_ITEM"] = EVENT_TYPE_SELECT_ITEM;

// Add below
	EventTypeMap["INSERT_ITEM_TOOLTIP_BY_CELL"] = EVENT_TYPE_INSERT_ITEM_TOOLTIP_BY_CELL;