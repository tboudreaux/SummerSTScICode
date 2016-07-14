from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[254.475042,32.081928],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1656+322/sdB_PG_1656+322_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1656+322/sdB_PG_1656+322_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
