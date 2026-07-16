from ns_dashboard.plots_ml import plot_xgb_feature_importance

def main():
    plot_xgb_feature_importance("models/swarm_xgb.json")

if __name__ == "__main__":
    main()

