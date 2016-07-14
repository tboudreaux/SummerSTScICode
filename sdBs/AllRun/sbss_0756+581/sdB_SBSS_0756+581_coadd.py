from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[120.164417,58.042889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_0756+581/sdB_SBSS_0756+581_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_0756+581/sdB_SBSS_0756+581_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
