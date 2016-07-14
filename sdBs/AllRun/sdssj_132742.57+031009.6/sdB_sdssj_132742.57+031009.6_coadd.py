from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[201.927375,3.169333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_132742.57+031009.6/sdB_sdssj_132742.57+031009.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_132742.57+031009.6/sdB_sdssj_132742.57+031009.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
