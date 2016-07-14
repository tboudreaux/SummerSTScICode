from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[354.329958,6.417778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_233719.19+062504.0/sdB_SDSSJ910_233719.19+062504.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_233719.19+062504.0/sdB_SDSSJ910_233719.19+062504.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
