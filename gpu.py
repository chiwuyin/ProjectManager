import torch
import torch.cuda.amp as amp

def benchmark_with_cuda_events(size, dtype=torch.float16, iterations=100):
    torch.cuda.init()
    torch.backends.cudnn.benchmark = True
    
    # 创建 CUDA events
    start_event = torch.cuda.Event(enable_timing=True)
    end_event = torch.cuda.Event(enable_timing=True)
    
    a = torch.randn(size, size, dtype=dtype, device='cuda').contiguous()
    b = torch.randn(size, size, dtype=dtype, device='cuda').contiguous()
    
    # 预热
    with amp.autocast():
        for _ in range(10):
            c = torch.matmul(a, b)
    
    # 测试
    start_event.record()
    with amp.autocast():
        for _ in range(iterations):
            c = torch.matmul(a, b)
    end_event.record()
    
    # 等待完成
    torch.cuda.synchronize()
    
    # 获取时间（毫秒）
    elapsed = start_event.elapsed_time(end_event) / 1000.0  # 转换为秒
    
    flops = 2 * size * size * size * iterations
    tflops = flops / (elapsed * 1e12)
    
    return tflops

def main():
    print(f"Testing on: {torch.cuda.get_device_name()}\n")
    print("Running optimized benchmark with CUDA events...")
    
    sizes = [1024, 2048, 4096, 8192,16384]
    for size in sizes:
        try:
            tflops = benchmark_with_cuda_events(size)
            print(f"Matrix size: {size}x{size}, TFLOPS: {tflops:.2f}")
        except RuntimeError as e:
            print(f"Size {size} failed: {e}")

if __name__ == "__main__":
    main()
