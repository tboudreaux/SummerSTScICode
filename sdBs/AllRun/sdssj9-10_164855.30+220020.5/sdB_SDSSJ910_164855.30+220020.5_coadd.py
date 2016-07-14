from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[252.230417,22.005694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_164855.30+220020.5/sdB_SDSSJ910_164855.30+220020.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_164855.30+220020.5/sdB_SDSSJ910_164855.30+220020.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
