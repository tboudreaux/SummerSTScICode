from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[160.14813,43.316931],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_0039+4302/sdB_HS_0039+4302_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_0039+4302/sdB_HS_0039+4302_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
