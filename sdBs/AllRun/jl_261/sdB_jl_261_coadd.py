from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[26.822667,-51.560856],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_jl_261/sdB_jl_261_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_jl_261/sdB_jl_261_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
