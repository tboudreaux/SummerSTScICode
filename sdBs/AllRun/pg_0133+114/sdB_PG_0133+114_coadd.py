from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[24.109417,11.658608],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_0133+114/sdB_PG_0133+114_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_0133+114/sdB_PG_0133+114_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
