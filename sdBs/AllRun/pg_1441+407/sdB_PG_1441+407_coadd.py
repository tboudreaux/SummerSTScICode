from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[220.838958,40.476389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1441+407/sdB_PG_1441+407_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1441+407/sdB_PG_1441+407_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
