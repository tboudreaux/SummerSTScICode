from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[333.849167,17.525728],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_2212+173/sdB_PG_2212+173_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_2212+173/sdB_PG_2212+173_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()