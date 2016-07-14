from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[262.226417,36.332944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_172854.34+361958.6/sdB_sdssj9-10_172854.34+361958.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_172854.34+361958.6/sdB_sdssj9-10_172854.34+361958.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
