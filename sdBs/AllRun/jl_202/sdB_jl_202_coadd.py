from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[10.055208,-55.031192],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_jl_202/sdB_jl_202_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_jl_202/sdB_jl_202_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
