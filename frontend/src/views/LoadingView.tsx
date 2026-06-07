import { LoadingSpinner } from "@components";

export default function LoadingView(): React.ReactNode {
  return (
    <div className="flex flex-1 items-center justify-center px-6 py-20">
      <LoadingSpinner className="text-body" />
    </div>
  );
}
