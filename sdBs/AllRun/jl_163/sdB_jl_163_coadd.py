from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[2.638375,-50.256781],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_jl_163/sdB_jl_163_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_jl_163/sdB_jl_163_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
