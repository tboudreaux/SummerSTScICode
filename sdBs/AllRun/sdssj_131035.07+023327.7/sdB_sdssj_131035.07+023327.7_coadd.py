from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[197.646125,2.557694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_131035.07+023327.7/sdB_sdssj_131035.07+023327.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_131035.07+023327.7/sdB_sdssj_131035.07+023327.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
