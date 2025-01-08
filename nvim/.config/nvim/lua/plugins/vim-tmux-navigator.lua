return {
	"christoomey/vim-tmux-navigator",
	cmd = {
		"TmuxNavigateLeft",
		"TmuxNavigateDown",
		"TmuxNavigateUp",
		"TmuxNavigateRight",
		"TmuxNavigatePrevious",
	},
	keys = {
		{ "<c-h>", "<cmd><C-U>TmuxNavigateLeft<cr>", desc = "Tmux: Navigate to the left pane" },
		{ "<c-j>", "<cmd><C-U>TmuxNavigateDown<cr>", desc = "Tmux: Navigate to the bottom pane" },
		{ "<c-k>", "<cmd><C-U>TmuxNavigateUp<cr>", desc = "Tmux: Navigate to the top pane" },
		{ "<c-l>", "<cmd><C-U>TmuxNavigateRight<cr>", desc = "Tmux: Navigate to the right pane" },
		{ "<c-\\>", "<cmd><C-U>TmuxNavigatePrevious<cr>", desc = "Tmux: Navigate to the previous pane" },
	},
}
