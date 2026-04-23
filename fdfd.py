import os
import sys

def print_tree(startpath):
    print(f"\n--- Project Structure: {os.path.abspath(startpath)} ---")
    for root, dirs, files in os.walk(startpath):
        # استثناء المجلدات غير الضرورية للتشخيص
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'venv']]
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f.endswith('.py'):
                print(f"{subindent}{f}")

def print_sys_path():
    print("\n--- Python sys.path (Priority Order) ---")
    for i, path in enumerate(sys.path):
        status = "✅ Exists" if os.path.exists(path) else "❌ Not Found"
        print(f"[{i}] {path} ({status})")

if __name__ == "__main__":
    # تشخيص المجلد الحالي
    print_tree('.')
    print_sys_path()
    
    print("\n--- Diagnostic Check ---")
    # محاولة فحص وجود الموديولات برمجياً
    modules_to_check = ['app', 'models', 'pipeline', 'services']
    for mod in modules_to_check:
        try:
            # محاولة العثور على مسار الموديول دون عمل import كامل
            import importlib.util
            spec = importlib.util.find_spec(mod)
            if spec:
                print(f"🔍 Module '{mod}': FOUND at {spec.origin}")
            else:
                print(f"🔍 Module '{mod}': NOT FOUND in current sys.path")
        except Exception as e:
            print(f"🔍 Module '{mod}': ERROR checking ({e})")