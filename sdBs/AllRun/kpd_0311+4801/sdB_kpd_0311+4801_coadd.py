from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[48.691417,48.201653],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kpd_0311+4801/sdB_kpd_0311+4801_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kpd_0311+4801/sdB_kpd_0311+4801_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
