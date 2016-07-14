from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[267.607917,24.952833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_175025.90+245710.2/sdB_sdssj_175025.90+245710.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_175025.90+245710.2/sdB_sdssj_175025.90+245710.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
