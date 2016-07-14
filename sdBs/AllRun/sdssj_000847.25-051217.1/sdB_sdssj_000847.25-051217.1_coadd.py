from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[2.196875,-5.20475],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_000847.25-051217.1/sdB_sdssj_000847.25-051217.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_000847.25-051217.1/sdB_sdssj_000847.25-051217.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
